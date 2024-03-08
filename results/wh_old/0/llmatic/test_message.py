from user import User
from message import Message, MessageType, MessageStatus
from datetime import datetime
def test_message():
    user1 = User(1, 'User 1')
    user2 = User(2, 'User 2')
    message = Message(1, user1, user2, 'Hello, User 2!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)
    assert message.message_id == 1
    assert message.sender == user1
    assert message.receiver == user2
    assert message.content == 'Hello, User 2!'
    assert message.status == MessageStatus.DELIVERED
    assert message.type == MessageType.TEXT
