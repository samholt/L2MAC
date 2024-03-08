import unittest
from gcs_app.profiles.profile import UserProfile


class TestProfiles(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile(1, 'user1', 'user1@example.com', 'John', 'Doe')

    def test_update_bio(self):
        self.user_profile.update_bio('New bio')
        self.assertEqual(self.user_profile.bio, 'New bio')

    def test_get_full_name(self):
        full_name = self.user_profile.get_full_name()
        self.assertEqual(full_name, 'John Doe')


if __name__ == '__main__':
    unittest.main()