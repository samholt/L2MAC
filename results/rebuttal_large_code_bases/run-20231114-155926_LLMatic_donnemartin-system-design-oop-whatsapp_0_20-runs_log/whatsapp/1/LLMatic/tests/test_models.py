import unittest
from app.models import User, Message, Group, Status
from cryptography.fernet import Fernet


class UserModelTest(unittest.TestCase):
	def setUp(self):
		self.user1 = User(email='test@test.com', password='test')
		self.user2 = User(email='test2@test.com', password='test')

	def test_password_setter(self):
		self.assertTrue(self.user1.password_hash is not None)

	def test_password_verification(self):
		self.assertTrue(self.user1.check_password('test'))
		self.assertFalse(self.user1.check_password('wrong'))

	def test_password_salts_are_random(self):
		self.assertTrue(self.user1.password_hash != self.user2.password_hash)

	def test_contact_blocking(self):
		self.user1.block_contact(self.user2)
		self.assertIn(self.user2, self.user1.blocked_contacts)

	def test_contact_unblocking(self):
		self.user1.block_contact(self.user2)
		self.user1.unblock_contact(self.user2)
		self.assertNotIn(self.user2, self.user1.blocked_contacts)


class MessageModelTest(unittest.TestCase):
	def setUp(self):
		self.user1 = User(email='test@test.com', password='test')
		self.user2 = User(email='test2@test.com', password='test')
		self.message = Message(sender=self.user1, recipient=self.user2, content='Hello', read_receipt=False, encryption_key=Fernet.generate_key().decode())

	def test_message_encryption(self):
		self.message.encrypt_content()
		self.assertNotEqual(self.message.content, 'Hello')

	def test_message_decryption(self):
		self.message.encrypt_content()
		self.message.decrypt_content()
		self.assertEqual(self.message.content, 'Hello')


class GroupModelTest(unittest.TestCase):
	def setUp(self):
		self.group = Group(name='test')
		self.user = User(email='participant@test.com', password='test')
		self.group.add_participant(self.user)
		self.group.set_admin(self.user)

	def test_group_participant_addition(self):
		self.assertIn(self.user, self.group.participants)

	def test_group_participant_removal(self):
		self.group.remove_participant(self.user)
		self.assertNotIn(self.user, self.group.participants)

	def test_group_admin_addition(self):
		self.assertIn(self.user, self.group.admins)

	def test_group_admin_removal(self):
		self.group.remove_admin(self.user)
		self.assertNotIn(self.user, self.group.admins)


class StatusModelTest(unittest.TestCase):
	def setUp(self):
		self.user = User(email='user@test.com', password='test')
		self.status = Status(user=self.user, content='Hello', visibility=True)

	def test_status_visibility(self):
		self.status.set_visibility(False)
		self.assertFalse(self.status.visibility)
		self.status.set_visibility(True)
		self.assertTrue(self.status.visibility)


if __name__ == '__main__':
	unittest.main()

