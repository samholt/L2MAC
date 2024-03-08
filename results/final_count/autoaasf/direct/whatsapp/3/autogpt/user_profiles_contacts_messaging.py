class UserProfile:
    def __init__(self, user):
        self.user = user
        self.contacts = set()
        self.messages = {}

    def add_contact(self, contact):
        self.contacts.add(contact)

    def remove_contact(self, contact):
        self.contacts.discard(contact)

    def send_message(self, recipient, message):
        if recipient not in self.contacts:
            return False
        if recipient not in self.messages:
            self.messages[recipient] = []
        self.messages[recipient].append(message)
        return True

    def get_messages(self, contact):
        if contact not in self.contacts:
            return None
        return self.messages.get(contact, [])