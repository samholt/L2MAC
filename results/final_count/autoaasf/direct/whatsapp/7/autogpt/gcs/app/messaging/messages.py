class Message:
    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content


class Messaging:
    def __init__(self):
        pass

    def send_message(self, sender_id, receiver_id, content):
        # TODO: Implement message sending logic
        pass

    def fetch_messages(self, user_id):
        # TODO: Implement message fetching logic
        pass
