import unittest
from cloudsafe.share.models import Share
from cloudsafe.share.views import generate_shareable_link, manage_shared_folder


class TestShare(unittest.TestCase):
    def setUp(self):
        self.share = Share('file', ['user1', 'user2'], 'read', '2022-12-31', True, 'password')

    def test_generate_shareable_link(self):
        link = self.share.generate_shareable_link()
        self.assertIsNotNone(link)

    def test_manage_shared_folder(self):
        self.share.manage_shared_folder()
        self.assertTrue(self.share)
