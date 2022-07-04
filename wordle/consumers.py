import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .views import Match

class WordleConsumer(WebsocketConsumer):

    def connect(self):
        match_id = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'match_' + match_id

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        match = Match.objects.get(pk=match_id)

        if match.has_started:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'get_game_data'
                }
            )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'update_game':
            from_id = text_data_json['from_id']
            attempts = text_data_json['opponent_attempts']
            colors = text_data_json['opponent_colors']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'update_game',
                    'attempts': attempts,
                    'colors': colors,
                    'from_id': from_id
                }
            )
        
        if text_data_json['type'] == 'give_game_data':
            from_id = text_data_json['from_id']
            attempts = text_data_json['attempts']
            colors = text_data_json['colors']
            opponent_attempts = text_data_json['opponent_attempts']
            opponent_colors = text_data_json['opponent_colors']

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'give_game_data',
                    'attempts': attempts,
                    'colors': colors,
                    'opponent_attempts': opponent_attempts,
                    'opponent_colors': opponent_colors,
                    'from_id': from_id
                }
            )

    
    def update_game(self, event):
        attempts = event['attempts']
        colors = event['colors']
        from_id = event['from_id']

        self.send(text_data=json.dumps({
            'type': 'update_game',
            'opponent_attempts': attempts,
            'opponent_colors': colors,
            'from_id': from_id
        }))

    def get_game_data(self, event):
        self.send(text_data=json.dumps({
            'type': 'get_game_data'
        }))

    def give_game_data(self, event):
        self.send(text_data=json.dumps({
            'type': 'give_game_data',
            'attempts': event['attempts'],
            'colors': event['colors'],
            'opponent_attempts': event['opponent_attempts'],
            'opponent_colors': event['opponent_colors'],
            'from_id': event['from_id']
        }))