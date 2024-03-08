import datetime

class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f'{self.sender}: {self.content} ({self.timestamp.strftime("%Y-%m-%d %H:%M:%S")})'

class Messaging:
    def __init__(self, user):
        self.user = user
        self.conversations = {}

    def send_message(self, recipient, content):
        message = Message(self.user, recipient, content)
        if recipient not in self.conversations:
            self.conversations[recipient] = []
        self.conversations[recipient].append(message)

    def get_conversation(self, contact):
        return self.conversations.get(contact, [])