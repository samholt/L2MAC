class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.blocked_users = set()
        self.groups = {}

    def block_user(self, user):
        self.blocked_users.add(user)

    def unblock_user(self, user):
        self.blocked_users.remove(user)

    def create_group(self, name, participants):
        self.groups[name] = {'participants': participants, 'picture': None}

    def edit_group(self, name, new_name=None, new_picture=None):
        if new_name:
            self.groups[new_name] = self.groups.pop(name)
            name = new_name
        if new_picture:
            self.groups[name]['picture'] = new_picture

    def add_participant(self, name, participant):
        self.groups[name]['participants'].add(participant)

    def remove_participant(self, name, participant):
        self.groups[name]['participants'].remove(participant)