class ContactService:
    def __init__(self):
        self.contacts = {}
        self.groups = {}

    def block_contact(self, user_id, contact_id):
        if user_id not in self.contacts:
            self.contacts[user_id] = set()
        self.contacts[user_id].add(contact_id)
        return True

    def unblock_contact(self, user_id, contact_id):
        if user_id in self.contacts and contact_id in self.contacts[user_id]:
            self.contacts[user_id].remove(contact_id)
            return True
        return False

    def create_group(self, user_id, group_name):
        if user_id not in self.groups:
            self.groups[user_id] = {}
        group_id = len(self.groups[user_id]) + 1
        self.groups[user_id][group_id] = {'name': group_name, 'members': set()}
        return group_id

    def edit_group(self, user_id, group_id, new_group_name):
        if user_id in self.groups and group_id in self.groups[user_id]:
            self.groups[user_id][group_id]['name'] = new_group_name
            return True
        return False

    def add_member_to_group(self, user_id, group_id, member_id):
        if user_id in self.groups and group_id in self.groups[user_id]:
            self.groups[user_id][group_id]['members'].add(member_id)
            return True
        return False

    def remove_member_from_group(self, user_id, group_id, member_id):
        if user_id in self.groups and group_id in self.groups[user_id] and member_id in self.groups[user_id][group_id]['members']:
            self.groups[user_id][group_id]['members'].remove(member_id)
            return True
        return False
