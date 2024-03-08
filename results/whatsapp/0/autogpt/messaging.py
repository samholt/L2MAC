import time


class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = time.time()


class MessageManager:
    def __init__(self):
        self.messages = {}

    def send_message(self, sender, recipient, content):
        message = Message(sender, recipient, content)
        if sender not in self.messages:
            self.messages[sender] = []
        if recipient not in self.messages:
            self.messages[recipient] = []
        self.messages[sender].append(message)
        self.messages[recipient].append(message)

    def get_messages(self, username):
        return self.messages.get(username, [])