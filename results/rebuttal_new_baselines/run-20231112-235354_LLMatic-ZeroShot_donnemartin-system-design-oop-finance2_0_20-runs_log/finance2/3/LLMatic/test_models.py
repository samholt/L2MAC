import unittest
from models import user, transaction, budget, investment, alert

class TestModels(unittest.TestCase):
	def test_user(self):
		user1 = user.User('John Doe', 'johndoe@example.com', 'password')
		self.assertEqual(user1.name, 'John Doe')
		self.assertEqual(user1.email, 'johndoe@example.com')

	def test_transaction(self):
		transaction1 = transaction.Transaction('John Doe', 100, 'income')
		self.assertEqual(transaction1.user, 'John Doe')
		self.assertEqual(transaction1.amount, 100)
		self.assertEqual(transaction1.category, 'income')

	def test_budget(self):
		budget1 = budget.Budget('John Doe', 1000, 'groceries')
		self.assertEqual(budget1.get_user_budgets('John Doe'), { 'amount': 1000, 'category': 'groceries' })

	def test_investment(self):
		investment1 = investment.Investment('John Doe', 10000, 'stocks')
		self.assertEqual(investment1.user, 'John Doe')
		self.assertEqual(investment1.amount, 10000)
		self.assertEqual(investment1.type, 'stocks')

	def test_alert(self):
		alert1 = alert.Alert('John Doe', 'Low balance', 'Your balance is low')
		self.assertEqual(alert1.user, 'John Doe')
		self.assertEqual(alert1.alert_type, 'Low balance')
		self.assertEqual(alert1.message, 'Your balance is low')
