# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators

import uuid


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    players = models.ManyToManyField(Player)
    created = models.DateTimeField(auto_now_add=True)


class Score(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    frame = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(11)])
    attempt = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(2)])
    value = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'player', 'frame', 'attempt')
