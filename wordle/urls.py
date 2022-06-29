from django.urls import path
from platformdirs import user_log_path
from .views import JoinMatchView

urlpatterns = [
    path('join', JoinMatchView)
]