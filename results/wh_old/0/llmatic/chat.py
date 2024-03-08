from typing import List
from message import Message

class Chat:
    def __init__(self):
        self.messages: List[Message] = []

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def update_message_status(self, message_id: int, status: str):
        for message in self.messages:
            if message.message_id == message_id:
                message.status = status
                break
