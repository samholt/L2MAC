import unittest
from status import Status

class TestStatus(unittest.TestCase):
	def setUp(self):
		self.status = Status('user1', 'image1.jpg', 24, ['user2', 'user3'])

	def test_post_image_status(self):
		self.status.post_image_status('image2.jpg', 48)
		self.assertEqual(self.status.image, 'image2.jpg')
		self.assertEqual(self.status.visibility_time, 48)

	def test_manage_viewers(self):
		self.status.manage_viewers(['user4', 'user5'])
		self.assertEqual(self.status.viewers, ['user4', 'user5'])

if __name__ == '__main__':
	unittest.main()
