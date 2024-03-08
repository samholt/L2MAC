from datetime import datetime
from typing import List


class Message:
    def __init__(self, sender_id: int, receiver_id: int, content: str):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = datetime.now()


class Conversation:
    def __init__(self, user1_id: int, user2_id: int):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.messages = []

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_messages(self) -> List[Message]:
        return self.messages