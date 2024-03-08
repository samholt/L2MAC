import unittest
from user_auth import register
from user_profiles import create_user_profile
from contact_management import create_contact_list


class TestContactManagement(unittest.TestCase):
    def test_contact_management(self):
        username1 = 'testuser1'
        password1 = 'testpassword1'
        user1 = register(username1, password1)
        display_name1 = 'Test User 1'
        status1 = 'Hello, world!'
        user_profile1 = create_user_profile(user1, display_name1, status1)

        username2 = 'testuser2'
        password2 = 'testpassword2'
        user2 = register(username2, password2)
        display_name2 = 'Test User 2'
        status2 = 'Hello, world!'
        user_profile2 = create_user_profile(user2, display_name2, status2)

        contact_list = create_contact_list()
        contact_list.add_contact(user_profile1)
        contact_list.add_contact(user_profile2)

        self.assertEqual(contact_list.get_contact(username1), user_profile1)
        self.assertEqual(contact_list.get_contact(username2), user_profile2)

        contact_list.remove_contact(username1)
        self.assertIsNone(contact_list.get_contact(username1))


if __name__ == '__main__':
    unittest.main()