import unittest
from cloudsafe.models.shared_link import SharedLink
from cloudsafe.models.file import File


class TestSharedLink(unittest.TestCase):
	def setUp(self):
		file = File('test_file', 'txt', 'test_content', 'root', [], [])
		self.shared_link = SharedLink(file, '2022-12-31', 'password')
	
	def test_shared_link_creation(self):
		self.assertEqual(self.shared_link.id, 'test_file')
		self.assertEqual(self.shared_link.item.id, 'test_file')
		self.assertEqual(self.shared_link.expiry_date, '2022-12-31')
		self.assertEqual(self.shared_link.password, 'password')
