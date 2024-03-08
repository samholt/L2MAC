from user import User
from message import Message, MessageType, MessageStatus
from chat import Chat
from group_chat import GroupChat
from notification import Notification
from encryption import Encryption
from datetime import datetime

def main():
    # Create users
    user1 = User(1, 'User 1')
    user2 = User(2, 'User 2')
    user3 = User(3, 'User 3')

    # Create chat
    chat = Chat()

    # Create group chat
    group_chat = GroupChat(1, 'Group 1', [user1, user2, user3])

    # Create messages
    message1 = Message(1, user1, user2, 'Hello, User 2!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)
    message2 = Message(2, user2, user1, 'Hello, User 1!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)

    # Add messages to chat
    chat.add_message(message1)
    chat.add_message(message2)

    # Create group message
    group_message = Message(3, user1, None, 'Hello, Group 1!', datetime.now(), MessageStatus.DELIVERED, MessageType.TEXT)

    # Add group message to group chat
    group_chat.add_message(group_message)

    # Create notification
    notification = Notification(1, user2, message1, 'unread')

    # Send notification
    notification.send_notification()

    # Create encryption
    encryption = Encryption()

    # Encrypt and decrypt message
    encrypted_message = encryption.encrypt(message1.content)
    decrypted_message = encryption.decrypt(encrypted_message)

    print(f'Original message: {message1.content}')
    print(f'Encrypted message: {encrypted_message}')
    print(f'Decrypted message: {decrypted_message}')

if __name__ == '__main__':
    main()
