class GroupChat:
    def __init__(self, name, creator, picture=None):
        self.name = name
        self.creator = creator
        self.picture = picture
        self.participants = {creator}
        self.admins = {creator}

    def add_participant(self, participant):
        self.participants.add(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)

    def add_admin(self, admin):
        if admin in self.participants:
            self.admins.add(admin)

    def remove_admin(self, admin):
        if admin != self.creator:
            self.admins.remove(admin)

class GroupChatManagement:
    def __init__(self):
        self.group_chats = {}

    def create_group_chat(self, name, creator, picture=None):
        self.group_chats[name] = GroupChat(name, creator, picture)