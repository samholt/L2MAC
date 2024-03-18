
# Update User class to support online/offline status
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.online = False

    def go_online(self):
        self.online = True

    def go_offline(self):
        self.online = False

# Update Chat class to support message queuing
class Chat:
    def __init__(self):
        self.messages = []
        self.queue = []

    def send_message(self, sender, recipient, text):
        message = Message(sender, recipient, text)
        if recipient.online:
            self.messages.append(message)
        else:
            self.queue.append(message)

    def deliver_queued_messages(self, recipient):
        for message in self.queue:
            if message.recipient == recipient:
                self.messages.append(message)
                self.queue.remove(message)