from attr import fields
from rest_framework.serializers import ModelSerializer
from .models import Match, Player

class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'players', 'player_count', 'to_guess']

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['tag']