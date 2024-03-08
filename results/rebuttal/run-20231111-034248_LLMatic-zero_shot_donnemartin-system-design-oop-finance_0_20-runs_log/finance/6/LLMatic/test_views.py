from views import UserView, TransactionView, BankAccountView, BudgetView, InvestmentView
from models import Category, Transaction, Budget, Investment, User
from datetime import datetime

def test_user_view():
	user_view = UserView()
	user = User('Test User', 'test@example.com', 'password')
	assert user_view.view_savings_tips(user) == 'Save more, spend less!'
	assert user_view.view_product_recommendations(user) == 'Consider investing in stocks.'
	assert user_view.view_notifications(user) == 'You have an upcoming bill due tomorrow.'
	assert user_view.view_alerts(user) == 'Unusual activity detected in your account.'

def test_transaction_view():
	transaction_view = TransactionView()
	assert transaction_view.view_monthly_report(1) == {'Test Category': 400}
	assert transaction_view.view_spending_trends() == {2022: {'Test Category': 300}, 2023: {'Test Category': 300}}
	assert transaction_view.view_year_on_year_comparison(2022, 2023) == {'Test Category': {'year1': 300, 'year2': 300}}

def test_bank_account_view():
	bank_account_view = BankAccountView()
	assert bank_account_view.view_account_balance('Test Account') == 'Account balance: $1000'

def test_budget_view():
	budget_view = BudgetView()
	assert budget_view.create_budget('Test User', 1000) == 'Budget created successfully'

def test_investment_view():
	investment_view = InvestmentView()
	assert investment_view.view_investment_performance('Test Investment') == 'Investment performance: 10% return'
