class SavingsTips:
	def __init__(self):
		self.savings_tips_db = {}

	def add_savings_tip(self, username, savings_tip):
		if username not in self.savings_tips_db:
			self.savings_tips_db[username] = []
		self.savings_tips_db[username].append(savings_tip)
		return 'Savings tip added successfully'

	def get_savings_tips(self, username):
		if username in self.savings_tips_db:
			return self.savings_tips_db[username]
		else:
			return 'No savings tips available'

