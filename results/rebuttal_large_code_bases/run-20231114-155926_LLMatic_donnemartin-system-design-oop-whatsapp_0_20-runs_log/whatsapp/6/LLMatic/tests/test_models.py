import unittest
from app.models import User, Message, Group, Status
from datetime import datetime
from cryptography.fernet import Fernet
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class TestUser(unittest.TestCase):
	def setUp(self):
		self.user = User()
		self.user.id = 1
		self.user.username = 'test@test.com'
		self.user.password_hash = 'password'
		self.user.profile_picture = 'profile_picture.jpg'
		self.user.status_message = 'Hello!'
		self.user.privacy_settings = 'public'
		self.user.blocked_contacts = []

	def test_set_password(self):
		self.user.set_password('new_password')
		self.assertTrue(self.user.check_password('new_password'))

	def test_block_contact(self):
		self.user.block_contact('contact1')
		self.assertIn('contact1', self.user.blocked_contacts)

	def test_unblock_contact(self):
		self.user.block_contact('contact1')
		self.user.unblock_contact('contact1')
		self.assertNotIn('contact1', self.user.blocked_contacts)

	def test_get_reset_password_token(self):
		token = self.user.get_reset_password_token('secret_key')
		self.assertIsNotNone(token)

	def test_verify_reset_password_token(self):
		token = self.user.get_reset_password_token('secret_key')
		verified = User.verify_reset_password_token(token, 'secret_key')
		self.assertEqual(verified, self.user.id)


class TestMessage(unittest.TestCase):
	def setUp(self):
		self.sender = User()
		self.sender.id = 1
		self.sender.username = 'sender@test.com'
		self.sender.password_hash = 'password'
		self.sender.profile_picture = 'profile_picture.jpg'
		self.sender.status_message = 'Hello!'
		self.sender.privacy_settings = 'public'
		self.sender.blocked_contacts = []
		self.receiver = User()
		self.receiver.id = 2
		self.receiver.username = 'receiver@test.com'
		self.receiver.password_hash = 'password'
		self.receiver.profile_picture = 'profile_picture.jpg'
		self.receiver.status_message = 'Hello!'
		self.receiver.privacy_settings = 'public'
		self.receiver.blocked_contacts = []
		self.message = Message()
		self.message.id = 1
		self.message.sender_id = self.sender.id
		self.message.receiver_id = self.receiver.id
		self.message.content = 'Hello!'
		self.message.timestamp = datetime.now()
		self.message.read_receipt = False
		self.message.encryption = False

	def test_encrypt_decrypt_content(self):
		with app.app_context():
			key = Fernet.generate_key()
			self.message.encrypt_content(key)
			self.assertNotEqual(self.message.content, 'Hello!')
			self.message.decrypt_content(key)
			self.assertEqual(self.message.content, 'Hello!')


class TestGroup(unittest.TestCase):
	def setUp(self):
		self.group = Group()
		self.group.id = 1
		self.group.name = 'Group1'
		self.group.picture = 'group_picture.jpg'
		self.group.participants = []
		self.group.admins = []

	def test_add_remove_participant(self):
		with app.app_context():
			self.group.add_participant('user1')
			self.assertIn('user1', self.group.participants)
			self.group.remove_participant('user1')
			self.assertNotIn('user1', self.group.participants)

	def test_assign_revoke_admin(self):
		with app.app_context():
			self.group.add_participant('user1')
			self.group.assign_admin('user1')
			self.assertIn('user1', self.group.admins)
			self.group.revoke_admin('user1')
			self.assertNotIn('user1', self.group.admins)


class TestStatus(unittest.TestCase):
	def setUp(self):
		self.user = User()
		self.user.id = 1
		self.user.username = 'user@test.com'
		self.user.password_hash = 'password'
		self.user.profile_picture = 'profile_picture.jpg'
		self.user.status_message = 'Hello!'
		self.user.privacy_settings = 'public'
		self.user.blocked_contacts = []
		self.status = Status()
		self.status.id = 1
		self.status.user_id = self.user.id
		self.status.image = 'status_image.jpg'
		self.status.timestamp = datetime.now()
		self.status.visibility = 'public'

	def test_set_visibility(self):
		self.status.set_visibility('private')
		self.assertEqual(self.status.visibility, 'private')


if __name__ == '__main__':
	unittest.main()

