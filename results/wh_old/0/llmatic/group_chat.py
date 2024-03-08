from typing import List
from user import User
from chat import Chat
from message import Message

class GroupChat(Chat):
    def __init__(self, group_id: int, group_name: str, members: List[User]):
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name
        self.members = members

    def add_message(self, message: Message):
        if message.sender in self.members:
            super().add_message(message)
        else:
            raise ValueError("Sender is not a member of the group")

    def get_messages(self):
        return super().get_messages()
