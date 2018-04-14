# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from serializers import GameSerializer, ScoreSerializer, PlayerSerializer
from models import Game, Score, Player


@api_view(['GET', 'POST'])
def game_root(request):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
    elif request.method == 'POST':
        game = Game()
        game.save()
        serializer = GameSerializer(game)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def players_root(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def game_scores(request, game_id):
    if request.method == 'GET':
        try:
            scores = Score.objects.get(game__id=game_id)
        except Score.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ScoreSerializer(scores)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data.copy()
        data['game'] = game_id
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
