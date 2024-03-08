class Notification:
	def __init__(self, type, message):
		self.type = type
		self.message = message

	def send_email(self, email):
		# Mock sending email
		print(f'Sending {self.type} notification to {email} with message: {self.message}')

	def send_sms(self, phone_number):
		# Mock sending sms
		print(f'Sending {self.type} notification to {phone_number} with message: {self.message}')

	def set_reminder(self, time):
		# Mock setting reminder
		print(f'Setting a {self.type} reminder at {time} with message: {self.message}')
