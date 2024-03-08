class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, user, contact):
        if user.username not in self.contacts:
            self.contacts[user.username] = set()
        self.contacts[user.username].add(contact.username)

    def remove_contact(self, user, contact):
        if user.username in self.contacts and contact.username in self.contacts[user.username]:
            self.contacts[user.username].remove(contact.username)

    def get_contacts(self, user):
        return self.contacts.get(user.username, set())