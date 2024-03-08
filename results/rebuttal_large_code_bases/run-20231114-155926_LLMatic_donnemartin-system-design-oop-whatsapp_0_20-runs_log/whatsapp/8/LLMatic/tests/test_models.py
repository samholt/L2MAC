import unittest
from flask import Flask
from app.models import User, Message, Group, Status


class TestUserModel(unittest.TestCase):

	def setUp(self):
		self.app = Flask(__name__)
		self.app.config['WTF_CSRF_SECRET_KEY'] = 'test'
		self.context = self.app.app_context()
		self.context.push()
		self.user = User(id=1, email='test@test.com', password='', profile_picture='', status_message='', privacy_settings='', last_seen_status='')

	def tearDown(self):
		self.context.pop()

	def test_check_password(self):
		self.user.set_password('test')
		self.assertTrue(self.user.check_password('test'))
		self.assertFalse(self.user.check_password('wrong'))

	def test_generate_recovery_token(self):
		self.assertEqual(self.user.generate_recovery_token(), 'recovery_token')


class TestMessageModel(unittest.TestCase):

	def setUp(self):
		self.app = Flask(__name__)
		self.app.config['WTF_CSRF_SECRET_KEY'] = 'test'
		self.context = self.app.app_context()
		self.context.push()
		self.user = User(id=1, email='test@test.com', password='', profile_picture='', status_message='', privacy_settings='', last_seen_status='')
		self.message = Message(id=1, sender=self.user, recipient=self.user, group_id=1, content='Hello', timestamp='', read_receipt=False, encryption_key='', image='', emoji='', gif='', sticker='')

	def tearDown(self):
		self.context.pop()

	def test_encrypt_decrypt_content(self):
		self.message.encrypt_content()
		encrypted_content = self.message.content
		self.assertNotEqual(encrypted_content, 'Hello')
		self.message.decrypt_content()
		self.assertEqual(self.message.content, 'Hello')


class TestGroupModel(unittest.TestCase):

	def setUp(self):
		self.app = Flask(__name__)
		self.app.config['WTF_CSRF_SECRET_KEY'] = 'test'
		self.context = self.app.app_context()
		self.context.push()
		self.user = User(id=1, email='test@test.com', password='', profile_picture='', status_message='', privacy_settings='', last_seen_status='')
		self.group = Group(id=1, name='Test Group', picture='', participants=[])

	def tearDown(self):
		self.context.pop()

	def test_add_remove_participant(self):
		self.group.add_participant(self.user)
		self.assertIn(self.user, self.group.participants)
		self.group.remove_participant(self.user)
		self.assertNotIn(self.user, self.group.participants)


if __name__ == '__main__':
	unittest.main()

