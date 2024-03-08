class Connectivity:
	def __init__(self):
		self.online_users = set()
		self.offline_messages = {}

	def go_online(self, user):
		self.online_users.add(user)
		if user in self.offline_messages:
			return self.offline_messages.pop(user)
		return []

	def go_offline(self, user):
		self.online_users.remove(user)

	def send_message(self, sender, receiver, content):
		if receiver in self.online_users:
			return True
		else:
			if receiver not in self.offline_messages:
				self.offline_messages[receiver] = []
			self.offline_messages[receiver].append((sender, content))
			return False
