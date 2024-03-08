import unittest
from controllers.transaction_controller import TransactionController
from controllers.user_controller import UserController
from models.transaction import Transaction


class TestTransactionController(unittest.TestCase):
	def test_create_transaction(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		transaction = TransactionController.create_transaction(user, 100, 'debit', 'groceries')
		self.assertIsInstance(transaction, Transaction)

	def test_get_transactions(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		TransactionController.create_transaction(user, 100, 'debit', 'groceries')
		transactions = TransactionController.get_transactions(user)
		self.assertIsInstance(transactions, list)

	def test_categorize_transaction(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		transaction = TransactionController.create_transaction(user, 100, 'debit', 'groceries')
		TransactionController.categorize_transaction(transaction, 'food')
		self.assertEqual(transaction.category, 'food')
