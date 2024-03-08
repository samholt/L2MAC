import unittest
from models.group import Group

class TestGroup(unittest.TestCase):
	def setUp(self):
		self.group = Group('1', 'Test Group', 'test.jpg', ['1', '2'], ['1'])

	def test_group_id(self):
		self.assertEqual(self.group.id, '1')

	def test_group_name(self):
		self.assertEqual(self.group.name, 'Test Group')

	def test_group_picture(self):
		self.assertEqual(self.group.picture, 'test.jpg')

	def test_group_participants(self):
		self.assertEqual(self.group.participants, ['1', '2'])

	def test_group_admin_roles(self):
		self.assertEqual(self.group.admin_roles, ['1'])

if __name__ == '__main__':
	unittest.main()
