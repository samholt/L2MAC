class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.contacts = []
        self.blocked_contacts = []
        self.groups = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def block_contact(self, contact):
        self.blocked_contacts.append(contact)
        self.contacts.remove(contact)

    def unblock_contact(self, contact):
        self.blocked_contacts.remove(contact)
        self.contacts.append(contact)

    def create_group(self, group):
        self.groups.append(group)