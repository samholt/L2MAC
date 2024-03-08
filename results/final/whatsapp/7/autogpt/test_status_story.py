import unittest
import time
from user_auth import register
from user_profiles import create_user_profile
from status_story import create_status_story


class TestStatusStory(unittest.TestCase):
    def test_status_story(self):
        username = 'testuser'
        password = 'testpassword'
        user = register(username, password)
        display_name = 'Test User'
        status = 'Hello, world!'
        user_profile = create_user_profile(user, display_name, status)

        content = 'My first status'
        duration = 86400
        status_story = create_status_story(user_profile, content, duration)

        self.assertEqual(status_story.user_profile, user_profile)
        self.assertEqual(status_story.content, content)
        self.assertEqual(status_story.duration, duration)
        self.assertFalse(status_story.is_expired())

        time.sleep(1)
        status_story.duration = 0
        self.assertTrue(status_story.is_expired())


if __name__ == '__main__':
    unittest.main()