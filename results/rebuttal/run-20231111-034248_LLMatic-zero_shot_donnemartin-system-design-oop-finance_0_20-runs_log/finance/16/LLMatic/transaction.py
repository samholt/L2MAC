class Transaction:
	def __init__(self, user, amount, category, type):
		self.user = user
		self.amount = amount
		self.category = category
		self.type = type
		self.recurring = False

	def enter_transaction(self):
		# Enter transaction into the system
		return 'Transaction entered'

	def upload_transaction(self):
		# Upload transaction data
		return 'Transaction data uploaded'

	def categorize_transaction(self):
		# Categorize the transaction
		return 'Transaction categorized'

	def classify_recurring(self):
		# Classify the transaction as recurring
		self.recurring = True
		return 'Transaction classified as recurring'
