class Notification:
	def __init__(self, notification_type, content):
		self.notification_type = notification_type
		self.content = content

	def send_email(self, email):
		# Mock sending email
		print(f'Sending email to {email} with content: {self.content}')

	def send_sms(self, phone_number):
		# Mock sending sms
		print(f'Sending sms to {phone_number} with content: {self.content}')

	def set_reminder(self, reminder_time):
		# Mock setting reminder
		print(f'Setting reminder for {reminder_time} with content: {self.content}')
