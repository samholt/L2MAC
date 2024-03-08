class GroupChat:
    def __init__(self, name):
        self.name = name
        self.members = set()
        self.messages = []

    def add_member(self, user_profile):
        self.members.add(user_profile)

    def remove_member(self, user_profile):
        self.members.discard(user_profile)

    def add_message(self, sender, content):
        if sender in self.members:
            message = Message(sender, None, content)
            self.messages.append(message)


def create_group_chat(name):
    return GroupChat(name)