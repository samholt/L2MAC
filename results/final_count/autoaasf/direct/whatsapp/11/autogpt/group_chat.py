class GroupChat:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.members = {creator}
        self.messages = []

    def add_member(self, member):
        self.members.add(member)

    def remove_member(self, member):
        if member != self.creator:
            self.members.discard(member)

    def send_message(self, sender, content):
        if sender in self.members:
            message = Message(sender, self.name, content)
            self.messages.append(message)

    def get_messages(self):
        return self.messages