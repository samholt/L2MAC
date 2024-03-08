import unittest
from models.user import User
from models.transaction import Transaction
from models.budget import Budget
from models.investment import Investment
from models.alert import Alert

class TestModels(unittest.TestCase):
	def test_user(self):
		user = User('John Doe', 'johndoe@example.com', 'password')
		self.assertEqual(user.username, 'John Doe')
		self.assertEqual(user.email, 'johndoe@example.com')
		self.assertTrue(user.check_password('password'))
		verification_code = user.generate_verification_code()
		self.assertEqual(len(verification_code), 6)
		self.assertTrue(user.verify(verification_code))

	def test_transaction(self):
		transaction = Transaction('John Doe', 100, 'income')
		self.assertEqual(transaction.user, 'John Doe')
		self.assertEqual(transaction.amount, 100)
		self.assertEqual(transaction.type, 'income')

	def test_budget(self):
		budget = Budget('John Doe', 1000)
		self.assertEqual(budget.user, 'John Doe')
		self.assertEqual(budget.amount, 1000)

	def test_investment(self):
		investment = Investment('John Doe', 1000, 'stocks')
		self.assertEqual(investment.user, 'John Doe')
		self.assertEqual(investment.amount, 1000)
		self.assertEqual(investment.type, 'stocks')

	def test_alert(self):
		alert = Alert('John Doe', 'Low balance')
		self.assertEqual(alert.user, 'John Doe')
		self.assertEqual(alert.message, 'Low balance')
