class UserStatus:
    def __init__(self, user):
        self.user = user
        self.online = False
        self.last_seen = None

    def set_online(self):
        self.online = True
        self.last_seen = None

    def set_offline(self):
        self.online = False
        self.last_seen = time.time()


class MessageQueue:
    def __init__(self):
        self.queue = []

    def add_message(self, message):
        self.queue.append(message)

    def get_messages(self):
        messages = self.queue
        self.queue = []
        return messages