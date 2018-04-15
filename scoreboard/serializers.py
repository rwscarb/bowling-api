from rest_framework import serializers

from models import Game, Score, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'created')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        depth = 1
        fields = ('id', 'players', 'score_set', 'created')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'player', 'game', 'frame', 'attempt', 'value', 'created')
