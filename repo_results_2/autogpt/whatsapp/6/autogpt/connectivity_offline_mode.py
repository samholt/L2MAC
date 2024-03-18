class ConnectivityOfflineMode:
    def __init__(self, user):
        self.user = user
        self.online = True
        self.message_queue = []

    def go_offline(self):
        self.online = False

    def go_online(self):
        self.online = True
        self.send_queued_messages()

    def send_message(self, message):
        if self.online:
            # send message
            pass
        else:
            self.message_queue.append(message)

    def send_queued_messages(self):
        while self.message_queue:
            message = self.message_queue.pop(0)
            # send message