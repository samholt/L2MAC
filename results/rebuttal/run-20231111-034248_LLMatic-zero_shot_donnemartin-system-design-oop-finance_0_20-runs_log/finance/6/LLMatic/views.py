from services import UserService, TransactionService, BankAccountService, BudgetService, InvestmentService

user_service = UserService()
transaction_service = TransactionService()
bank_account_service = BankAccountService()
budget_service = BudgetService()
investment_service = InvestmentService()

class UserView:
	# existing code...

	def view_savings_tips(self, user):
		return user_service.generate_savings_tips(user)

	def view_product_recommendations(self, user):
		return user_service.recommend_products(user)

	def view_notifications(self, user):
		return user_service.send_notifications(user)

	def view_alerts(self, user):
		return user_service.alert_unusual_activity(user)

class TransactionView:
	# existing code...

	def view_monthly_report(self, month):
		return transaction_service.generate_monthly_report(month)

	def view_spending_trends(self):
		return transaction_service.visualize_spending_trends()

	def view_year_on_year_comparison(self, year1, year2):
		return transaction_service.compare_year_on_year(year1, year2)

class BankAccountView:
	# existing code...

	def view_account_balance(self, account):
		return bank_account_service.get_balance(account)

class BudgetView:
	def __init__(self):
		pass

	def create_budget(self, user, amount):
		return budget_service.create_budget(user, amount)

class InvestmentView:
	# existing code...

	def view_investment_performance(self, investment):
		return investment_service.get_performance(investment)
