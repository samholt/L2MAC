class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, username, contact_username):
        if username not in self.contacts:
            self.contacts[username] = set()
        self.contacts[username].add(contact_username)

    def remove_contact(self, username, contact_username):
        if username in self.contacts and contact_username in self.contacts[username]:
            self.contacts[username].remove(contact_username)

    def get_contacts(self, username):
        return self.contacts.get(username, set())