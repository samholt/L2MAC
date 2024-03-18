class User:
    def __init__(self, name):
        self.name = name
        self.online = False
        self.message_queue = []

    def go_online(self):
        self.online = True
        self.process_queue()

    def go_offline(self):
        self.online = False

    def process_queue(self):
        while self.message_queue:
            message = self.message_queue.pop(0)
            print(f'Processing message: {message}')

    def receive_message(self, message):
        if self.online:
            print(f'Received message: {message}')
        else:
            self.message_queue.append(message)