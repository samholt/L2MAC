class GroupChat:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.members = {creator.username}
        self.messages = []

    def add_member(self, user):
        self.members.add(user.username)

    def remove_member(self, user):
        if user.username != self.creator.username:
            self.members.discard(user.username)

    def add_message(self, message):
        self.messages.append(message)


class GroupChatManager:
    def __init__(self):
        self.group_chats = {}

    def create_group_chat(self, name, creator):
        group_chat = GroupChat(name, creator)
        self.group_chats[group_chat.name] = group_chat
        return group_chat

    def get_group_chat(self, name):
        return self.group_chats.get(name, None)