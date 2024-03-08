import datetime

class Alert:
	def __init__(self, user_id, message):
		self.user_id = user_id
		self.message = message
		self.date = datetime.datetime.now()

	def to_dict(self):
		return {
			'user_id': self.user_id,
			'message': self.message,
			'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
		}
