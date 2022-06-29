from django.urls import path
from .consumers import WordleConsumer

websocket_urlpatterns = [
    path('ws/socket-server/<room_name>', WordleConsumer.as_asgi())
]