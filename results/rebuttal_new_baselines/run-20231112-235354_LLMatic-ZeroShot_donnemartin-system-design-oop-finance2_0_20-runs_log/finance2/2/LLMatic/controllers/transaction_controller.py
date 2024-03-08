from models.transaction import Transaction


class TransactionController:
	@staticmethod
	def create_transaction(user, amount, type, category):
		return Transaction.create(user, amount, type, category)

	@staticmethod
	def get_transactions(user):
		return Transaction.get_transactions(user)

	@staticmethod
	def categorize_transaction(transaction, category):
		return Transaction.categorize(transaction, category)
