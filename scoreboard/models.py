# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators
from django.contrib import admin

import uuid


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    players = models.ManyToManyField(Player)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# todo: validate 11th frame can't be submitted unless 10th is STRIKE/SPARE
# todo: validate out of order frames, e.g. first submitted frame is frame#9
# todo: pass backend magic numbers to frontend
class Score(models.Model):
    class Meta:
        unique_together = ('game', 'player', 'frame', 'attempt')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    frame = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(11)])
    attempt = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(2)])
    value = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        self.clean()
        super(Score, self).save(*args, **kwargs)

    def __str__(self):
        return '{game}/{player} F{frame:02}-A{attempt:02}-{value}'.format(
            game=self.game_id, player=self.player_id, frame=self.frame, attempt=self.attempt, value=self.value)


@admin.register(Score)
class ScoreModelAdmin(admin.ModelAdmin):
    pass
