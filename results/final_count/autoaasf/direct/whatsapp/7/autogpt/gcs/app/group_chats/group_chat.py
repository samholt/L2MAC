class GroupChat:
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
        self.participants = set()

    def add_participant(self, user_id):
        # TODO: Implement participant addition logic
        pass

    def remove_participant(self, user_id):
        # TODO: Implement participant removal logic
        pass


class GroupChatManager:
    def __init__(self):
        pass

    def create_group_chat(self, group_name):
        # TODO: Implement group chat creation logic
        pass

    def delete_group_chat(self, group_id):
        # TODO: Implement group chat deletion logic
        pass
