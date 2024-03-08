import unittest
from user_auth import register
from user_profiles import create_user_profile
from messaging import create_conversation


class TestMessaging(unittest.TestCase):
    def test_messaging(self):
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

        conversation = create_conversation(user_profile1, user_profile2)
        content = 'Hello, Test User 2!'
        conversation.add_message(user_profile1, user_profile2, content)

        self.assertEqual(conversation.messages[0].sender, user_profile1)
        self.assertEqual(conversation.messages[0].recipient, user_profile2)
        self.assertEqual(conversation.messages[0].content, content)


if __name__ == '__main__':
    unittest.main()