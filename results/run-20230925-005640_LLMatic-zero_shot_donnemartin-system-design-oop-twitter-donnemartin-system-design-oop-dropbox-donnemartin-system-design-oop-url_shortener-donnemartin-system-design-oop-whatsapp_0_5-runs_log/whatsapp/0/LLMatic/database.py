class Database:
	users = {}
	statuses = []
	groups = []
	messages = []

	@classmethod
	def add_user(cls, user):
		cls.users[user.email] = user

	@classmethod
	def add_status(cls, status):
		cls.statuses.append(status)

	@classmethod
	def add_group(cls, group):
		cls.groups.append(group)

	@classmethod
	def add_message(cls, message):
		cls.messages.append(message)
		if message.queued and message.receiver.online:
			message.queued = False
