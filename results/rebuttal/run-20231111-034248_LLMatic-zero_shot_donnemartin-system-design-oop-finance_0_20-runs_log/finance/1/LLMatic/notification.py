class Notification:
	def __init__(self):
		self.notification_db = {}
		self.bill_alerts_db = {}
		self.fraud_alerts_db = {}

	def send_notification(self, user_id, message):
		if user_id not in self.notification_db:
			self.notification_db[user_id] = []
		self.notification_db[user_id].append(message)

	def get_notifications(self, user_id):
		if user_id in self.notification_db:
			return self.notification_db[user_id]
		return []

	def set_bill_alert(self, user_id, bill_due_date, message):
		if user_id not in self.bill_alerts_db:
			self.bill_alerts_db[user_id] = []
		self.bill_alerts_db[user_id].append((bill_due_date, message))

	def get_bill_alerts(self, user_id):
		if user_id in self.bill_alerts_db:
			return self.bill_alerts_db[user_id]
		return []

	def set_fraud_alert(self, user_id, unusual_activity):
		if user_id not in self.fraud_alerts_db:
			self.fraud_alerts_db[user_id] = []
		self.fraud_alerts_db[user_id].append(unusual_activity)

	def get_fraud_alerts(self, user_id):
		if user_id in self.fraud_alerts_db:
			return self.fraud_alerts_db[user_id]
		return []
