from user import User
from message import Message, MessageType, MessageStatus
from chat import Chat
from datetime import datetime
def test_chat():
    chat = Chat()
    user1 = User(1, 'User 1')
    user2 = User(2, 'User 2')
    message = Message(1, user1, user2, 'Hello, User 2!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)
    chat.add_message(message)
    assert len(chat.get_messages()) == 1
    chat.update_message_status(1, MessageStatus.READ)
    assert chat.get_messages()[0].status == MessageStatus.READ
