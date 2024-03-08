class Contacts:
	def __init__(self):
		self.users = {}

	def block_unblock_contact(self, user_email, contact_email):
		if user_email not in self.users:
			self.users[user_email] = {'blocked_contacts': [], 'groups': {}}
		if contact_email in self.users[user_email]['blocked_contacts']:
			self.users[user_email]['blocked_contacts'].remove(contact_email)
		else:
			self.users[user_email]['blocked_contacts'].append(contact_email)

	def manage_group(self, user_email, group_name, emails):
		if user_email not in self.users:
			self.users[user_email] = {'blocked_contacts': [], 'groups': {}}
		self.users[user_email]['groups'][group_name] = emails
