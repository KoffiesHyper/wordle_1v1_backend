import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class WordleConsumer(WebsocketConsumer):

    def connect(self):
        match_id = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'match_' + match_id

        print(self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
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
    
    def update_game(self, event):
        attempts = event['attempts']
        colors = event['colors']
        from_id = event['from_id']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'opponent_attempts': attempts,
            'opponent_colors': colors,
            'from_id': from_id
        }))