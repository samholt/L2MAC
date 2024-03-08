import time


class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = time.time()


class Conversation:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.messages = []

    def add_message(self, sender, recipient, content):
        message = Message(sender, recipient, content)
        self.messages.append(message)


def create_conversation(user1, user2):
    return Conversation(user1, user2)