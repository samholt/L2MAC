import unittest
from controllers.budget_controller import BudgetController
from controllers.user_controller import UserController
from models.budget import Budget


class TestBudgetController(unittest.TestCase):
	def test_create_budget(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		budget = BudgetController.create_budget(user, 1000, 'groceries', 'January')
		self.assertIsInstance(budget, Budget)

	def test_set_budget(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		budget = BudgetController.create_budget(user, 1000, 'groceries', 'January')
		BudgetController.set_budget(budget, 1500)
		self.assertEqual(budget.amount, 1500)

	def test_adjust_budget(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		budget = BudgetController.create_budget(user, 1000, 'groceries', 'January')
		BudgetController.adjust_budget(budget, 500)
		self.assertEqual(budget.amount, 1500)

	def test_is_limit_nearing(self):
		user = UserController.create_user('John Doe', 'john@example.com', 'password')
		budget = BudgetController.create_budget(user, 1000, 'groceries', 'January')
		self.assertFalse(BudgetController.is_limit_nearing(budget, 90))
