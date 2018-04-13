# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators

import uuid


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Score(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    frame = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(11)])
    attempt = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(2)])
    value = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])
