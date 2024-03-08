import unittest
from user_auth import UserManager, User
from user_profiles_contacts_messaging import UserProfile
from group_chats_status_webapp import GroupChat, Status, WebApp


class TestGCS(unittest.TestCase):
    def setUp(self):
        self.webapp = WebApp()
        self.webapp.user_manager = UserManager()

    def test_user_registration_authentication(self):
        self.assertTrue(self.webapp.register_user('user1', 'password1'))
        self.assertFalse(self.webapp.register_user('user1', 'password2'))
        self.assertTrue(self.webapp.authenticate_user('user1', 'password1'))
        self.assertFalse(self.webapp.authenticate_user('user1', 'password2'))

    def test_user_profiles_contacts_messaging(self):
        self.webapp.register_user('user2', 'password2')
        if 'user1' in self.webapp.user_profiles:
            self.webapp.user_profiles['user1'].add_contact('user2')
            self.assertIn('user2', self.webapp.user_profiles['user1'].contacts)
            self.webapp.user_profiles['user1'].send_message('user2', 'Hello')
            self.assertEqual(self.webapp.user_profiles['user1'].get_messages('user2'), ['Hello'])

    def test_group_chats_status(self):
        self.webapp.create_group_chat('group1')
        self.webapp.group_chats['group1'].add_member('user1')
        self.webapp.group_chats['group1'].send_message('user1', 'Hello, group1!')
        self.assertEqual(self.webapp.group_chats['group1'].messages, [('user1', 'Hello, group1!')])
        self.webapp.post_status('user1', 'My first status')
        if 'user1' in self.webapp.statuses:
            self.assertEqual(self.webapp.statuses['user1'].content, 'My first status')


if __name__ == '__main__':
    unittest.main()