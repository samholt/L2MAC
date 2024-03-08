class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.connection_status = False

    def send_message(self, receiver, content):
        pass  # To be implemented

    def receive_message(self, message):
        pass  # To be implemented
