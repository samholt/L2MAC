class Contact:
    def __init__(self, user_id: int, username: str, full_name: str):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, user_id: int):
        self.contacts = [contact for contact in self.contacts if contact.user_id != user_id]

    def search_contact(self, search_term: str):
        return [contact for contact in self.contacts if search_term.lower() in contact.username.lower() or search_term.lower() in contact.full_name.lower()]