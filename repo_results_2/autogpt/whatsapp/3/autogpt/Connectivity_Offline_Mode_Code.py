class User:
    def __init__(self, name):
        self.name = name
        self.online = False
        self.message_queue = []

    def go_online(self):
        self.online = True
        self.deliver_messages()

    def go_offline(self):
        self.online = False

    def send_message(self, recipient, message):
        if recipient.online:
            recipient.receive_message(message)
        else:
            recipient.message_queue.append(message)

    def receive_message(self, message):
        # Implement message receiving logic here
        pass

    def deliver_messages(self):
        while self.message_queue:
            self.receive_message(self.message_queue.pop(0))