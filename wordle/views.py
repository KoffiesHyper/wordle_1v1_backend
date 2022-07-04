import math
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from .serializers import MatchSerializer, PlayerSerializer
from .models import Player, Match

# Create your views here.

@api_view(['POST'])
def GetMatchView(request, match_id):
    match = Match.objects.get(pk=match_id)
    serializer = MatchSerializer(match)
    return Response(serializer.data)

@api_view(['POST'])
def JoinMatchView(request):
    newPlayer = Player(tag=request.data['data']['tag'])
    newPlayer.save()

    to_guess = request.data['data']['to_guess']

    match = Match.objects.filter(player_count=1).first()

    if match:
        match.add_player(newPlayer)
        match.player_count = 2
        match.has_started=True
        match.to_guess = match.to_guess + '.' + to_guess
        match.save()
        serializer = MatchSerializer(match)
        return Response(serializer.data)
    else:
        match = Match(player_count=1)
        match.to_guess = to_guess
        match.save()
        match.add_player(newPlayer)
        serializer = MatchSerializer(match)
        return Response(serializer.data)

@api_view(['GET'])
def PlayerTagsView(request, match_id):
    match = Match.objects.get(pk=match_id)
    serializer = PlayerSerializer(match.players.all(), many=True)
    return Response(serializer.data)

