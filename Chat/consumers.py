import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async 
import errno 
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join the room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
       

    async def disconnect(self, close_code):
        print(f"WebSocket connection closed with code: {close_code}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
    )

      

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        print("message",message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    