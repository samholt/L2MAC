class GroupChat:
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        self.members = [admin]
        self.messages = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def add_message(self, message):
        self.messages.append(message)