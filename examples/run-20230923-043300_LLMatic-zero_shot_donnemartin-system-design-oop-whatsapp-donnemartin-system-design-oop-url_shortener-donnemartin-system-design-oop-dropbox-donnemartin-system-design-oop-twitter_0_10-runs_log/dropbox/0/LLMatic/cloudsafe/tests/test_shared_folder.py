import unittest
from cloudsafe.models.shared_folder import SharedFolder
from cloudsafe.models.user import User
from cloudsafe.models.folder import Folder

class TestSharedFolder(unittest.TestCase):
	def setUp(self):
		self.shared_folder = SharedFolder(id=1, users=[], permissions=[], folder=Folder(id=1, name='folder', creation_date='2022-01-01', owner=1))

	def test_invite_user(self):
		user = User(id=2, name='user', email='user@example.com', password='password', profile_picture='profile.jpg', storage_used=0)
		self.shared_folder.invite_user(user)
		self.assertIn(user, self.shared_folder.users)

	def test_set_permissions(self):
		user = User(id=2, name='user', email='user@example.com', password='password', profile_picture='profile.jpg', storage_used=0)
		self.shared_folder.set_permissions(user, ['view', 'edit'])
		self.assertEqual(self.shared_folder.permissions, ['view', 'edit'])
