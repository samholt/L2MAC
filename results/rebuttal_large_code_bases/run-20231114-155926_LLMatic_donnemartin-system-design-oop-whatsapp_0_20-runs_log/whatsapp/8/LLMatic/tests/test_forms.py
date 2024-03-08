import unittest
from flask import Flask
from app.forms import LoginForm, RegistrationForm, RecoverPasswordForm, ResetPasswordForm, EditProfileForm, BlockForm, GroupForm, SendMessageForm, PostStatusForm
from app.database import MockDatabase


class TestForms(unittest.TestCase):

	def setUp(self):
		self.db = MockDatabase()
		self.app = Flask(__name__)
		self.app.config['WTF_CSRF_SECRET_KEY'] = 'test'
		self.context = self.app.app_context()
		self.context.push()

	def tearDown(self):
		self.context.pop()

	def test_registration_form(self):
		form = RegistrationForm()
		self.assertFalse(form.validate())

	def test_login_form(self):
		form = LoginForm()
		self.assertFalse(form.validate())

	def test_password_recovery_form(self):
		form = RecoverPasswordForm()
		self.assertFalse(form.validate())

	def test_password_reset_form(self):
		form = ResetPasswordForm()
		self.assertFalse(form.validate())

	def test_profile_form(self):
		form = EditProfileForm()
		self.assertFalse(form.validate())

	def test_block_form(self):
		form = BlockForm()
		self.assertFalse(form.validate())

	def test_group_form(self):
		form = GroupForm()
		self.assertFalse(form.validate())

	def test_message_form(self):
		form = SendMessageForm()
		self.assertFalse(form.validate())

	def test_status_form(self):
		form = PostStatusForm()
		self.assertFalse(form.validate())


if __name__ == '__main__':
	unittest.main()

