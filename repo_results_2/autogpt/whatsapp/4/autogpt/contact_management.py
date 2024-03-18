class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.contacts = {}
        self.groups = {}

    def add_contact(self, contact):
        self.contacts[contact.email] = contact

    def block_contact(self, contact):
        self.contacts[contact.email].blocked = True

    def unblock_contact(self, contact):
        self.contacts[contact.email].blocked = False

    def create_group(self, group_name):
        self.groups[group_name] = []

    def add_to_group(self, group_name, contact):
        self.groups[group_name].append(contact)

    def remove_from_group(self, group_name, contact):
        self.groups[group_name].remove(contact)