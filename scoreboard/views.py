# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from serializers import GameSerializer, ScoreSerializer, PlayerSerializer
from models import Game, Score, Player


def api_helper(request, uid, model, serializer):
    if request.method == 'GET':
        if uid is not None:
            instance = model.objects.get(id=uid)
            serial = serializer(instance)
        else:
            objects = model.objects.all()
            serial = serializer(objects, many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = serializer(data=request.data)
        if serial.is_valid(raise_exception=True):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serial = serializer(data=request.data)
        instance = model.objects.get(id=uid)
        if serial.is_valid(raise_exception=True):
            serial.update(instance, serial.validated_data)
            return Response(serial.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT'])
def players_api(request, player_id=None):
    return api_helper(request, player_id, Player, PlayerSerializer)


@api_view(['GET', 'POST'])
def games_api(request, game_id=None):
    return api_helper(request, game_id, Game, GameSerializer)


@api_view(['GET', 'POST'])
def scores_api(request, score_id=None):
    return api_helper(request, score_id, Score, ScoreSerializer)
