import unittest
from models.transaction import Transaction
from datetime import datetime


class TestTransaction(unittest.TestCase):
	def setUp(self):
		self.transaction = Transaction.create('test_user', 100, 'groceries')

	def test_create(self):
		self.assertEqual(self.transaction.user, 'test_user')
		self.assertEqual(self.transaction.amount, 100)
		self.assertEqual(self.transaction.category, 'groceries')
		self.assertIsInstance(self.transaction.date, datetime)

	def test_get_user_transactions(self):
		# This should interact with a real database
		# For now, we'll use a mock in-memory database
		transactions = Transaction.get_user_transactions('test_user')
		self.assertIsInstance(transactions, list)

	def test_categorize(self):
		self.transaction.categorize('entertainment')
		self.assertEqual(self.transaction.category, 'entertainment')
