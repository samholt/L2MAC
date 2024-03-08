import unittest
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):
	def setUp(self):
		self.user = 'test_user'
		self.amount = 100
		self.category = 'groceries'
		self.transaction = Transaction.create_transaction(self.user, self.amount, self.category)
		self.transactions = [self.transaction]

	def test_create_transaction(self):
		self.assertEqual(self.transaction.user, self.user)
		self.assertEqual(self.transaction.amount, self.amount)
		self.assertEqual(self.transaction.category, self.category)

	def test_get_user_transactions(self):
		transactions = Transaction.get_user_transactions(self.user, self.transactions)
		self.assertTrue(all(transaction.user == self.user for transaction in transactions))

	def test_categorize_transactions(self):
		transactions = Transaction.categorize_transactions(Transaction.get_user_transactions(self.user, self.transactions), self.category)
		self.assertTrue(all(transaction.category == self.category for transaction in transactions))
