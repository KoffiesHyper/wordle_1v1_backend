from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MatchSerializer
from .models import Player, Match

# Create your views here.

@api_view(['GET', 'POST'])
def JoinMatchView(request):
    newPlayer = Player(tag=request.data['data']['tag'])
    newPlayer.save()

    match = Match.objects.filter(player_count=1).first()

    if match:
        match.add_player(newPlayer)
        match.player_count = 2
        match.started=True
        match.save()
        serializer = MatchSerializer(match)
        return Response(serializer.data)
    else:
        match = Match(player_count=1)
        match.save()
        match.add_player(newPlayer)
        serializer = MatchSerializer(match)
        return Response(serializer.data)

