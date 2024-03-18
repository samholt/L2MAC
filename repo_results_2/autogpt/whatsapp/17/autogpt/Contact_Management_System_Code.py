class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.contacts = []
        self.blocked_contacts = []
        self.groups = {}

    def block_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            self.blocked_contacts.append(contact)

    def unblock_contact(self, contact):
        if contact in self.blocked_contacts:
            self.blocked_contacts.remove(contact)
            self.contacts.append(contact)

    def create_group(self, group_name):
        self.groups[group_name] = []

    def edit_group(self, group_name, new_group_name):
        if group_name in self.groups:
            self.groups[new_group_name] = self.groups.pop(group_name)

    def manage_group(self, group_name, action, contact):
        if group_name in self.groups:
            if action == 'add':
                self.groups[group_name].append(contact)
            elif action == 'remove':
                self.groups[group_name].remove(contact)