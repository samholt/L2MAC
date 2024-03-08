class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

class Message:
    def __init__(self, sender, recipients, content, media=None):
        self.sender = sender
        self.recipients = recipients
        self.content = content
        self.media = media
        self.status = {}
        for recipient in recipients:
            self.status[recipient] = {'delivered': False, 'read': False}

class Conversation:
    def __init__(self, participants):
        self.participants = participants
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

class GroupConversation(Conversation):
    def __init__(self, participants, group_name):
        super().__init__(participants)
        self.group_name = group_name