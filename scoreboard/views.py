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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def game_scores(request, game_id):
    scores = Score.objects.get(game__id=game_id)
    serializer = ScoreSerializer(scores)

    return Response(serializer.data)
