from user import User
from message import Message, MessageType, MessageStatus
from group_chat import GroupChat
from datetime import datetime
def test_group_chat():
    user1 = User(1, 'User 1')
    user2 = User(2, 'User 2')
    user3 = User(3, 'User 3')
    group_chat = GroupChat(1, 'Group 1', [user1, user2, user3])
    message = Message(1, user1, None, 'Hello, Group 1!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)
    group_chat.add_message(message)
    assert len(group_chat.get_messages()) == 1
