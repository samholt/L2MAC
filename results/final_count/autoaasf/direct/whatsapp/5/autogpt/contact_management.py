class ContactManagement:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, user_id, user_profile):
        self.contacts[user_id] = user_profile

    def remove_contact(self, user_id):
        if user_id in self.contacts:
            del self.contacts[user_id]

    def get_contact(self, user_id):
        return self.contacts.get(user_id)


if __name__ == '__main__':
    contact_management = ContactManagement()
    contact_management.add_contact(1, {'username': 'test_user', 'email': 'test@example.com'})
    contact_management.remove_contact(1)