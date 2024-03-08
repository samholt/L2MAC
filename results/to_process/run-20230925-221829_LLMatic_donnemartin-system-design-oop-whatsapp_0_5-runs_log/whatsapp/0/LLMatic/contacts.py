class Contacts:
	def __init__(self):
		self.contacts_db = {}
		self.groups_db = {}

	def block_contact(self, user_id, contact_id):
		if user_id not in self.contacts_db:
			self.contacts_db[user_id] = {'blocked': [], 'groups': []}
		self.contacts_db[user_id]['blocked'].append(contact_id)

	def unblock_contact(self, user_id, contact_id):
		if user_id in self.contacts_db and contact_id in self.contacts_db[user_id]['blocked']:
			self.contacts_db[user_id]['blocked'].remove(contact_id)

	def create_group(self, user_id, group_name, contact_ids):
		if user_id not in self.contacts_db:
			self.contacts_db[user_id] = {'blocked': [], 'groups': []}
		group_id = len(self.groups_db) + 1
		self.groups_db[group_id] = {'name': group_name, 'contacts': contact_ids}
		self.contacts_db[user_id]['groups'].append(group_id)

	def edit_group(self, group_id, new_group_name, new_contact_ids):
		if group_id in self.groups_db:
			self.groups_db[group_id] = {'name': new_group_name, 'contacts': new_contact_ids}

	def manage_group(self, user_id, group_id):
		if user_id in self.contacts_db and group_id in self.contacts_db[user_id]['groups']:
			return self.groups_db[group_id]
		return None
