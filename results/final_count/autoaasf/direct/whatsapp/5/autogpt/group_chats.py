import time


class GroupChat:

    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
        self.members = []
        self.messages = []

    def add_member(self, user_id):
        if user_id not in self.members:
            self.members.append(user_id)

    def remove_member(self, user_id):
        if user_id in self.members:
            self.members.remove(user_id)

    def send_message(self, sender_id, content):
        if sender_id in self.members:
            message = {
                'sender_id': sender_id,
                'content': content,
                'timestamp': time.time()
            }
            self.messages.append(message)


if __name__ == '__main__':
    group_chat = GroupChat(1, 'Test Group')
    group_chat.add_member(1)
    group_chat.add_member(2)
    group_chat.send_message(1, 'Hello, everyone!')