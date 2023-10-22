import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import errno
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.user = self.scope['session'].get(
            'username')  # Get the authenticated user
        # The other user to chat with
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_name = get_common_room_name(self.user, self.username)
        self.room_group_name = f'{self.room_name}'

        print("roomname:", self.room_name)

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
        username = text_data_json['username']
    

        await self.save_message(message)

        loggedinUser = self.scope['session'].get('username')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'logged': loggedinUser,
                'username': username,
                
            }
        )

    async def save_message(self, message):

        from Chat.models import Messages
        from App.models import Register_table
        from Chat.models import Add_chat

        user = await sync_to_async(Register_table.objects.get)(username=self.user)
        user_id = user.id

        chat_with_user = await sync_to_async(Add_chat.objects.get)(user=user_id, username=self.username)
        room_name = self.room_name
        print("Loggedin user -> Other user:",user.username,"->",chat_with_user.username)
        print("message:", message)
        await create_message(message, user, chat_with_user, room_name)

    # Receive message from room group

    async def chat_message(self, event):
        message = event['message']
        loggedinUser = event['logged']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'logged': loggedinUser,

        }))


def get_common_room_name(username1, username2):
    # Create a unique room name based on the usernames
    if username1 < username2:
        return f"chat_{username1}_{username2}"
    else:
        return f"chat_{username2}_{username1}"


@sync_to_async
def get_user_from_Register_table(user):
    try:
        from App.models import Register_table
        return Register_table.objects.get(username=user)
    except Register_table.DoesNotExist:
        return None


@sync_to_async
def create_message(message, user, chat_with, room_name):
    from Chat.models import Messages
    Messages.objects.create(
        message=message,
        user=user,
        chat_with=chat_with,
        room_name=room_name
    )
