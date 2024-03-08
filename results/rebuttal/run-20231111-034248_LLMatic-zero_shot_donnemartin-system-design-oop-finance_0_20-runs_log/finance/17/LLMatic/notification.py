class Notification:
	def __init__(self):
		self.notifications = {}

	def add_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

	def clear_notifications(self, user_id):
		self.notifications[user_id] = []

	def send_bill_notification(self, user_id, bill):
		message = f"Upcoming bill: {bill['name']} due on {bill['due_date']}. Amount: {bill['amount']}"
		self.add_notification(user_id, message)

	def send_fraud_alert(self, user_id, transaction):
		message = f"Unusual activity detected: {transaction['description']} on {transaction['date']}. Amount: {transaction['amount']}"
		self.add_notification(user_id, message)
