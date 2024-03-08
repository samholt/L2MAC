class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, user_profile):
        self.contacts[user_profile.user.username] = user_profile

    def remove_contact(self, username):
        if username in self.contacts:
            del self.contacts[username]

    def get_contact(self, username):
        return self.contacts.get(username)


def create_contact_list():
    return ContactList()