import unittest
from app.models import User, Group, Status, Message, DATABASE
from datetime import datetime


class TestUser(unittest.TestCase):

	def setUp(self):
		self.user1 = User(1, 'user1', 'user1@example.com', 'password1')
		self.user2 = User(2, 'user2', 'user2@example.com', 'password2')
		DATABASE.clear()

	def test_user_creation(self):
		self.assertEqual(self.user1.id, 1)
		self.assertEqual(self.user1.username, 'user1')
		self.assertEqual(self.user1.email, 'user1@example.com')
		self.assertEqual(self.user1.password, 'password1')

		self.assertEqual(self.user2.id, 2)
		self.assertEqual(self.user2.username, 'user2')
		self.assertEqual(self.user2.email, 'user2@example.com')
		self.assertEqual(self.user2.password, 'password2')


class TestGroup(unittest.TestCase):

	def setUp(self):
		self.user1 = User(1, 'user1', 'user1@example.com', 'password1')
		self.user2 = User(2, 'user2', 'user2@example.com', 'password2')
		self.group = Group(1, 'group1', None, [])
		DATABASE.clear()

	def test_group_creation(self):
		self.assertEqual(self.group.id, 1)
		self.assertEqual(self.group.name, 'group1')
		self.assertIsNone(self.group.admin)
		self.assertEqual(self.group.members, [])

	def test_set_admin(self):
		self.group.set_admin(self.user1.id)
		self.assertEqual(self.group.admin, self.user1.id)

	def test_check_permission(self):
		self.group.set_admin(self.user1.id)
		self.assertTrue(self.group.check_permission(self.user1.id))
		self.assertFalse(self.group.check_permission(self.user2.id))


class TestStatus(unittest.TestCase):

	def setUp(self):
		self.user1 = User(1, 'user1', 'user1@example.com', 'password1')
		self.status = Status(1, self.user1.id, 'image1', 'public', datetime.now())
		DATABASE.clear()

	def test_status_creation(self):
		self.assertEqual(self.status.id, 1)
		self.assertEqual(self.status.user_id, self.user1.id)
		self.assertEqual(self.status.image, 'image1')
		self.assertEqual(self.status.visibility, 'public')

	def test_post(self):
		Status.post(self.user1.id, 'image2', 'private')
		status = DATABASE[1]
		self.assertEqual(status.id, 1)
		self.assertEqual(status.user_id, self.user1.id)
		self.assertEqual(status.image, 'image2')
		self.assertEqual(status.visibility, 'private')

	def test_set_visibility(self):
		self.status.set_visibility('private')
		self.assertEqual(self.status.visibility, 'private')


class TestMessage(unittest.TestCase):

	def setUp(self):
		self.user1 = User(1, 'user1', 'user1@example.com', 'password1')
		self.user2 = User(2, 'user2', 'user2@example.com', 'password2')
		self.message = Message.send(self.user1.id, self.user2.id, 'Hello')
		DATABASE.clear()

	def test_message_creation(self):
		self.assertEqual(self.message.id, 1)
		self.assertEqual(self.message.sender_id, self.user1.id)
		self.assertEqual(self.message.receiver_id, self.user2.id)
		self.assertEqual(self.message.content, 'Hello')
		self.assertTrue(self.message.queued)

	def test_send(self):
		Message.send(self.user1.id, self.user2.id, 'Hello')
		message = DATABASE[1]
		self.assertEqual(message.id, 1)
		self.assertEqual(message.sender_id, self.user1.id)
		self.assertEqual(message.receiver_id, self.user2.id)
		self.assertEqual(message.content, 'Hello')
		self.assertTrue(message.queued)

	def test_receive(self):
		self.message.receive()
		self.assertFalse(self.message.queued)


if __name__ == '__main__':
	unittest.main()
