from django.urls import path
from .views import JoinMatchView

urlpatterns = [
    path('join', JoinMatchView)
]