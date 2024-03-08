import unittest
from user_auth import register
from user_profiles import create_user_profile
from group_chat import create_group_chat


class TestGroupChat(unittest.TestCase):
    def test_group_chat(self):
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

        group_chat = create_group_chat('Test Group')
        group_chat.add_member(user_profile1)
        group_chat.add_member(user_profile2)

        self.assertIn(user_profile1, group_chat.members)
        self.assertIn(user_profile2, group_chat.members)

        group_chat.remove_member(user_profile1)
        self.assertNotIn(user_profile1, group_chat.members)


if __name__ == '__main__':
    unittest.main()