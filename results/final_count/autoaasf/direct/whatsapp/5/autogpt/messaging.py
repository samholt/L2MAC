import time


class Messaging:

    def __init__(self):
        self.messages = []

    def send_message(self, sender_id, recipient_id, content):
        message = {
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'content': content,
            'timestamp': time.time()
        }
        self.messages.append(message)

    def get_messages(self, user_id):
        return [msg for msg in self.messages if msg['sender_id'] == user_id or msg['recipient_id'] == user_id]


if __name__ == '__main__':
    messaging = Messaging()
    messaging.send_message(1, 2, 'Hello, how are you?')
    messaging.send_message(2, 1, 'I am fine, thank you!')