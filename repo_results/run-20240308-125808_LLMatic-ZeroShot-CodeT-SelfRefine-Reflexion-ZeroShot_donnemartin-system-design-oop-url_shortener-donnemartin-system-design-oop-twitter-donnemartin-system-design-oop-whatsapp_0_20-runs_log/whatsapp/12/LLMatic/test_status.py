import time
import unittest
from status import Status, remove_expired_statuses


class TestStatus(unittest.TestCase):
	def setUp(self):
		self.status_db = {}
		self.status_db['1'] = Status('user1', 'image1', duration=0.001)
		self.status_db['2'] = Status('user2', 'image2', duration=24)

	def test_change_visibility(self):
		self.status_db['1'].change_visibility('private')
		self.assertEqual(self.status_db['1'].visibility, 'private')

	def test_remove_expired_statuses(self):
		time.sleep(2)
		remove_expired_statuses(self.status_db)
		self.assertNotIn('1', self.status_db)
		self.assertIn('2', self.status_db)


if __name__ == '__main__':
	unittest.main()
