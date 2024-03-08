class GroupChat:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.messages = []

    def add_member(self, user):
        self.members.append(user)

    def remove_member(self, user):
        self.members.remove(user)

    def send_message(self, message):
        self.messages.append(message)