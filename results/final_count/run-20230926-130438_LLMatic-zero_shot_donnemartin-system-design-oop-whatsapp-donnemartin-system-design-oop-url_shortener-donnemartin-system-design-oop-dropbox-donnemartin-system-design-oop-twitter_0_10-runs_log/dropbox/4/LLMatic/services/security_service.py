from models.activity_log import ActivityLog


class SecurityService:
	def __init__(self):
		self.activity_logs = {}

	def log_activity(self, user, action):
		activity_log = ActivityLog(user, action)
		if user not in self.activity_logs:
			self.activity_logs[user] = []
		self.activity_logs[user].append(activity_log)

	def get_activity_logs(self, user):
		return self.activity_logs.get(user, [])

	def encrypt(self, data):
		# Placeholder for encryption logic
		return data

	def decrypt(self, data):
		# Placeholder for decryption logic
		return data
