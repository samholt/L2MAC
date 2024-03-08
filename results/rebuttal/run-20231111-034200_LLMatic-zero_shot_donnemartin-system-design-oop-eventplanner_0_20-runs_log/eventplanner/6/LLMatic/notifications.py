class Notification:
	def __init__(self, type, message, time):
		self.type = type
		self.message = message
		self.time = time

	def send_email_notification(self, email, message):
		print(f'Sending email to {email} with message: {message}')

	def send_sms_notification(self, phone_number, message):
		print(f'Sending SMS to {phone_number} with message: {message}')

	def set_reminder(self, time, message):
		print(f'Setting reminder for {time} with message: {message}')


# Mock database
notifications_db = {}
