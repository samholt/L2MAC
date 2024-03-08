from typing import List
from gcs_app.messaging.messaging import Message


class GroupChat:
    def __init__(self, group_id: int, group_name: str):
        self.group_id = group_id
        self.group_name = group_name
        self.members = []
        self.messages = []

    def add_member(self, user_id: int):
        self.members.append(user_id)

    def remove_member(self, user_id: int):
        self.members.remove(user_id)

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_messages(self) -> List[Message]:
        return self.messages