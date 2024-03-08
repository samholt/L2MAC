class GroupChat:
    def __init__(self, name):
        self.name = name
        self.members = set()
        self.messages = []

    def add_member(self, username):
        self.members.add(username)

    def remove_member(self, username):
        if username in self.members:
            self.members.remove(username)

    def send_message(self, sender, content):
        if sender in self.members:
            message = Message(sender, self.name, content)
            self.messages.append(message)


class GroupChatManager:
    def __init__(self):
        self.group_chats = {}

    def create_group_chat(self, name):
        if name in self.group_chats:
            return False
        self.group_chats[name] = GroupChat(name)
        return True

    def get_group_chat(self, name):
        return self.group_chats.get(name, None)