from user import User
from message import Message, MessageType, MessageStatus
from notification import Notification
from datetime import datetime
def test_notification():
    user1 = User(1, 'User 1')
    user2 = User(2, 'User 2')
    message = Message(1, user1, user2, 'Hello, User 2!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)
    notification = Notification(1, user2, message, 'unread')
    assert notification.notification_id == 1
    assert notification.user == user2
    assert notification.message == message
    assert notification.status == 'unread'
