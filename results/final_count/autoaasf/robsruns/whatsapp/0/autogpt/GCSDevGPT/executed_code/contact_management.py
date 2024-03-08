class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.username] = contact

    def remove_contact(self, contact):
        if contact.username in self.contacts:
            del self.contacts[contact.username]