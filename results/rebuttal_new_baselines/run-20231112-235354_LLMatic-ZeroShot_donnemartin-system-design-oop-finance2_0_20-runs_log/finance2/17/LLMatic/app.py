from account import Account
from expense_income import Expense, Income
from budget import Budget
from investment import Investment
from reports import Reports
from database import MockDatabase

# Initialize the database
mock_db = MockDatabase()

# Create an instance of the User class
user_account = Account('John Doe', 10000)

# Link bank accounts
user_account.buy_asset('Bank Account', 5000)

# Enable multi-factor authentication
# This is a placeholder as the User class does not currently support multi-factor authentication

# Create instances of the Expense, Income, Budget, Investment, and Reports classes
user_expense = Expense()
user_income = Income()
user_budget = Budget()
user_investment = Investment()
user_reports = Reports(mock_db)

# Use their methods to manage expenses, incomes, budgets, investments, and reports
user_expense.import_expenses([{'name': 'Rent', 'amount': 1000}])
user_income.import_incomes([{'name': 'Salary', 'amount': 5000}])
user_budget.set_budget('Rent', 1200)
user_investment.integrate_account('John Doe', user_account)

# Add data to the mock database
mock_db.add('users', 'John Doe', {'balance': user_account.get_balance(), 'assets': user_account.get_assets()})
mock_db.add('expenses', 'John Doe', user_expense.visualize_expenses())
mock_db.add('incomes', 'John Doe', user_income.visualize_incomes())
mock_db.add('budgets', 'John Doe', {'Rent': user_budget.get_budget('Rent')})
mock_db.add('investments', 'John Doe', {'balance': user_investment.balance, 'performance': user_investment.performance})

# Generate financial report
financial_report = user_reports.generate_financial_report('John Doe')
mock_db.add('reports', 'John Doe', financial_report)
