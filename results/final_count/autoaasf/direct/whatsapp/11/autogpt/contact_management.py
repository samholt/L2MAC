class ContactManagement:
    def __init__(self, user):
        self.user = user
        self.contacts = {}

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts[contact] = UserProfile(contact, '', '', '', '')

    def remove_contact(self, contact):
        if contact in self.contacts:
            del self.contacts[contact]

    def get_contacts(self):
        return self.contacts