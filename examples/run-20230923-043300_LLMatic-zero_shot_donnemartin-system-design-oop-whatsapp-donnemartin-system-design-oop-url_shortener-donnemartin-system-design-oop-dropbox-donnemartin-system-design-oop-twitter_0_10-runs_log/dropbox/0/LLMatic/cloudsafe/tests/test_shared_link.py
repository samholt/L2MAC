import unittest
from cloudsafe.models.shared_link import SharedLink
from cloudsafe.models.file import File

class TestSharedLink(unittest.TestCase):
	def setUp(self):
		self.shared_link = SharedLink(id=1, url='http://example.com', expiry_date='2022-12-31', password='password', file=File(id=1, name='file.txt', size=100, type='txt', upload_date='2022-01-01', version=1, owner=1))

	def test_generate_link(self):
		self.shared_link.generate_link()
		self.assertIsNotNone(self.shared_link.url)

	def test_set_expiry_date(self):
		self.shared_link.set_expiry_date('2023-01-01')
		self.assertEqual(self.shared_link.expiry_date, '2023-01-01')

	def test_set_password(self):
		self.shared_link.set_password('new_password')
		self.assertEqual(self.shared_link.password, 'new_password')
