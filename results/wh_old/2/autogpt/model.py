class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class Message:
    def __init__(self, message_id, sender, content, timestamp):
        self.message_id = message_id
        self.sender = sender
        self.content = content
        self.timestamp = timestamp


class Chat:
    def __init__(self, chat_id, participants):
        self.chat_id = chat_id
        self.participants = participants
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def remove_message(self, message_id):
        self.messages = [msg for msg in self.messages if msg.message_id != message_id]