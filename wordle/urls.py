from django.urls import path
from .views import JoinMatchView, PlayerTagsView, GetMatchView

urlpatterns = [
    path('get-match/<int:match_id>', GetMatchView),
    path('join', JoinMatchView),
    path('get-player-tags/<int:match_id>', PlayerTagsView)
]