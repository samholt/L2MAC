import random
import string
from models.bank_account import BankAccount
from models.transaction import Transaction
from models.budget import Budget
from models.alert import Alert
from models.investment import Investment

class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.bank_accounts = {}
		self.transactions = {}
		self.budgets = {}
		self.alerts = []
		self.investments = {}

	def generate_verification_code(self):
		code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		self.verification_code = code
		return code

	def verify(self, code):
		return code == self.verification_code

	def add_bank_account(self, bank_name, account_number, balance):
		bank_account = BankAccount(bank_name, account_number, balance)
		self.bank_accounts[account_number] = bank_account

	def update_bank_account(self, account_number, new_bank_name=None, new_balance=None):
		bank_account = self.bank_accounts.get(account_number)
		if bank_account:
			if new_bank_name:
				bank_account.bank_name = new_bank_name
			if new_balance:
				bank_account.balance = new_balance
			return True
		return False

	def delete_bank_account(self, account_number):
		if account_number in self.bank_accounts:
			del self.bank_accounts[account_number]
			return True
		return False

	def add_transaction(self, amount, date, category, type):
		transaction = Transaction(self.username, amount, date, category, type)
		self.transactions[transaction.id] = transaction

	def update_transaction(self, transaction_id, new_amount=None, new_date=None, new_category=None, new_type=None):
		transaction = self.transactions.get(transaction_id)
		if transaction:
			transaction.update(new_amount, new_date, new_category, new_type)
			return True
		return False

	def delete_transaction(self, transaction_id):
		if transaction_id in self.transactions:
			del self.transactions[transaction_id]
			return True
		return False

	def get_transaction_history(self):
		transaction_history = sorted(self.transactions.values(), key=lambda t: t.date)
		return [{'id': t.id, 'amount': t.amount, 'date': t.date, 'category': t.category, 'type': t.type} for t in transaction_history]

	def add_budget(self, amount, month):
		budget = Budget(self.username, amount, month)
		self.budgets[month] = budget

	def update_budget(self, month, new_amount=None):
		budget = self.budgets.get(month)
		if budget:
			if new_amount:
				budget.amount = new_amount
			return True
		return False

	def delete_budget(self, month):
		if month in self.budgets:
			del self.budgets[month]
			return True
		return False

	def add_alert(self, message):
		alert = Alert(self.username, message)
		self.alerts.append(alert)

	def get_alerts(self):
		return [alert.to_dict() for alert in self.alerts]

	def add_investment(self, account_name, balance, asset_allocation):
		investment = Investment(account_name, balance, asset_allocation)
		self.investments[account_name] = investment

	def update_investment(self, account_name, new_balance=None, new_asset_allocation=None):
		investment = self.investments.get(account_name)
		if investment:
			if new_balance:
				investment.balance = new_balance
			if new_asset_allocation:
				investment.asset_allocation = new_asset_allocation
			return True
		return False

	def delete_investment(self, account_name):
		if account_name in self.investments:
			del self.investments[account_name]
			return True
		return False
