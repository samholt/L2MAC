import unittest
from controllers.investment_controller import InvestmentController
from models.investment import Investment


class TestInvestmentController(unittest.TestCase):
	def test_create_investment(self):
		investment = InvestmentController.create_investment('Account 1', 10000, {'stocks': 50, 'bonds': 50})
		self.assertIsInstance(investment, Investment)

	def test_link_account(self):
		investment = InvestmentController.create_investment('Account 1', 10000, {'stocks': 50, 'bonds': 50})
		InvestmentController.link_account(investment, 'Account 2')
		self.assertEqual(investment.account_name, 'Account 2')

	def test_track_performance(self):
		investment = InvestmentController.create_investment('Account 1', 10000, {'stocks': 50, 'bonds': 50})
		self.assertEqual(InvestmentController.track_performance(investment), 10000)

	def test_view_asset_allocation(self):
		investment = InvestmentController.create_investment('Account 1', 10000, {'stocks': 50, 'bonds': 50})
		self.assertEqual(InvestmentController.view_asset_allocation(investment), {'stocks': 50, 'bonds': 50})
