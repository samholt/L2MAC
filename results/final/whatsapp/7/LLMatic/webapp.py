from user import User
from contact import Contact
from message import Message
from group import Group
from status import Status


class WebApp:
	def __init__(self):
		self.users = {}
		self.contacts = {}
		self.messages = {}
		self.groups = {}
		self.statuses = {}

	def sign_up(self, email, password):
		# Implementation goes here
		pass

	def log_in(self, email, password):
		# Implementation goes here
		pass

	def recover_password(self, email):
		# Implementation goes here
		pass

	def view_profile(self, user_id):
		# Implementation goes here
		pass

	def edit_profile(self, user_id, new_profile):
		# Implementation goes here
		pass

	def block_contact(self, user_id, contact_id):
		# Implementation goes here
		pass

	def unblock_contact(self, user_id, contact_id):
		# Implementation goes here
		pass

	def create_group(self, user_id, group_name):
		# Implementation goes here
		pass

	def edit_group(self, group_id, new_group):
		# Implementation goes here
		pass

	def manage_group(self, group_id, action, user_id):
		# Implementation goes here
		pass

	def send_message(self, sender_id, receiver_id, message):
		# Implementation goes here
		pass

	def receive_message(self, receiver_id):
		# Implementation goes here
		pass

	def read_message(self, user_id, message_id):
		# Implementation goes here
		pass

	def share_image(self, user_id, image):
		# Implementation goes here
		pass

	def send_emoji(self, user_id, emoji):
		# Implementation goes here
		pass

	def create_group_chat(self, user_id, group_id):
		# Implementation goes here
		pass

	def add_participant(self, group_id, user_id):
		# Implementation goes here
		pass

	def remove_participant(self, group_id, user_id):
		# Implementation goes here
		pass

	def assign_admin_role(self, group_id, user_id):
		# Implementation goes here
		pass

	def remove_admin_role(self, group_id, user_id):
		# Implementation goes here
		pass

	def post_status(self, user_id, status):
		# Implementation goes here
		pass

	def view_status(self, user_id):
		# Implementation goes here
		pass

	def queue_message(self, sender_id, receiver_id, message):
		# Implementation goes here
		pass

	def display_online_status(self, user_id):
		# Implementation goes here
		pass
