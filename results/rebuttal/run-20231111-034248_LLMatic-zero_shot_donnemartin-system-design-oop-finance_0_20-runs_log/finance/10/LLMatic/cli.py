import sys
from user import User
from transaction import Transaction
from bank_account import BankAccount
from budget import Budget
from investment import Investment
from analytics import Analytics
from recommendations import Recommendations
from notifications import Notifications


class CLI:
	def __init__(self):
		self.user = User()
		self.transaction = Transaction()
		self.bank_account = BankAccount()
		self.budget = Budget()
		self.investment = Investment()
		self.analytics = Analytics()
		self.recommendations = Recommendations()
		self.notifications = Notifications()

	def run(self):
		while True:
			command = input('Enter command: ')
			if command == 'exit':
				break
			self.execute_command(command.split(' '))

	def execute_command(self, command):
		if command[0] == 'create_user':
			print(self.user.create_user(command[1], command[2]))
		elif command[0] == 'login':
			print(self.user.login(command[1], command[2]))
		elif command[0] == 'add_transaction':
			self.transaction.add_transaction(command[1], command[2])
		elif command[0] == 'link_account':
			self.bank_account.link_account(command[1], command[2])
		elif command[0] == 'set_budget':
			self.budget.set_monthly_budget(command[1], command[2])
		elif command[0] == 'add_investment':
			self.investment.add_investment(command[1], command[2])
		elif command[0] == 'view_analytics':
			print(self.analytics.generate_monthly_report(command[1]))
		elif command[0] == 'get_recommendations':
			print(self.recommendations.get_recommendations(command[1]))
		elif command[0] == 'get_notifications':
			print(self.notifications.get_notifications(command[1]))


if __name__ == '__main__':
	CLI().run()

