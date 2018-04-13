from rest_framework.serializers import ModelSerializer

from models import Game, Score, Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ('name',)


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('id',)


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ('game',)
