import unittest
from gcs_app.contacts.contacts import Contact, ContactList


class TestContacts(unittest.TestCase):
    def setUp(self):
        self.contact_list = ContactList()
        self.contact1 = Contact(1, 'user1', 'John Doe')
        self.contact2 = Contact(2, 'user2', 'Jane Doe')
        self.contact_list.add_contact(self.contact1)
        self.contact_list.add_contact(self.contact2)

    def test_add_contact(self):
        contact3 = Contact(3, 'user3', 'Jim Doe')
        self.contact_list.add_contact(contact3)
        self.assertIn(contact3, self.contact_list.contacts)

    def test_remove_contact(self):
        self.contact_list.remove_contact(1)
        self.assertNotIn(self.contact1, self.contact_list.contacts)

    def test_search_contact(self):
        search_results = self.contact_list.search_contact('Jane')
        self.assertIn(self.contact2, search_results)
        self.assertNotIn(self.contact1, search_results)


if __name__ == '__main__':
    unittest.main()