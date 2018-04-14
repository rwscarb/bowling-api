from rest_framework.serializers import ModelSerializer

from models import Game, Score, Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'created')


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'created')


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'player', 'game', 'frame', 'attempt', 'value', 'created')
