import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        formatted_timestamp = await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].username,
                'formatted_timestamp': formatted_timestamp,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        formatted_timestamp = event['formatted_timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'formatted_timestamp': formatted_timestamp,
        }))

    @database_sync_to_async
    def save_message(self, message):
        chat_room = ChatRoom.objects.get(name=self.room_name)
        sender = self.scope['user']

        new_message = Message(chat_room=chat_room, sender=sender, content=message)
        new_message.save()
        formatted_timestamp = new_message.formatted_timestamp()
        return formatted_timestamp

    @database_sync_to_async
    def get_or_create_room(self, user1_id, user2_id):
        user1 = get_user_model().objects.get(id=user1_id)
        user2 = get_user_model().objects.get(id=user2_id)
        chat_room = ChatRoom.get_or_create_chat_room(user1, user2)
        return chat_room