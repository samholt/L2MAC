import uuid
import time


class Message:
    def __init__(self, sender, recipient, content):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = time.time()


class MessageManager:
    def __init__(self):
        self.messages = {}

    def send_message(self, sender, recipient, content):
        message = Message(sender, recipient, content)
        if sender.username not in self.messages:
            self.messages[sender.username] = []
        if recipient.username not in self.messages:
            self.messages[recipient.username] = []
        self.messages[sender.username].append(message)
        self.messages[recipient.username].append(message)

    def get_messages(self, user):
        return self.messages.get(user.username, [])