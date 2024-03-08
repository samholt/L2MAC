class Message:
    def __init__(self, sender_id, content, timestamp):
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp


class Chat:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages


class OneOnOneChat(Chat):
    def __init__(self, user1_id, user2_id):
        super().__init__()
        self.user1_id = user1_id
        self.user2_id = user2_id


class GroupChat(Chat):
    def __init__(self, group_id, group_name):
        super().__init__()
        self.group_id = group_id
        self.group_name = group_name
        self.members = []

    def add_member(self, user_id):
        self.members.append(user_id)

    def remove_member(self, user_id):
        self.members.remove(user_id)