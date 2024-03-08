from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'secret'

# Mock database
users = {}
transactions = {}
budgets = {}
bank_accounts = {}

# User class
class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	@staticmethod
	def create_user(username, password, email):
		if username in users:
			return 'User already exists'
		users[username] = User(username, password, email)
		return 'User created successfully'

	@staticmethod
	def authenticate_user(username, password):
		if username in users and users[username].password == password:
			return True
		return False

# BankAccount class
class BankAccount:
	def __init__(self, bank_name, account_number, balance):
		self.bank_name = bank_name
		self.account_number = account_number
		self.balance = balance

	@staticmethod
	def add_bank_account(username, bank_name, account_number, balance):
		if username in users:
			bank_accounts[username] = BankAccount(bank_name, account_number, balance)
			return 'Bank account added successfully'
		return 'User does not exist'

	@staticmethod
	def update_balance(username, new_balance):
		if username in bank_accounts:
			bank_accounts[username].balance = new_balance
			return 'Balance updated successfully'
		return 'Bank account does not exist'

# Transaction class
class Transaction:
	def __init__(self, username, amount, category, date):
		self.username = username
		self.amount = amount
		self.category = category
		self.date = date

	@staticmethod
	def add_transaction(username, amount, category, date):
		if username in users:
			if username not in transactions:
				transactions[username] = []
			transactions[username].append(Transaction(username, amount, category, date))
			return 'Transaction added successfully'
		return 'User does not exist'

	@staticmethod
	def get_transactions(username):
		if username in transactions:
			return transactions[username]
		return 'No transactions found'

@app.route('/')
def home():
	return 'Home Page'

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if User.authenticate_user(data['username'], data['password']):
		session['username'] = data['username']
		return 'Login successful'
	return 'Invalid username or password'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	message = User.create_user(data['username'], data['password'], data['email'])
	return message

@app.route('/add_bank_account', methods=['POST'])
def add_bank_account():
	data = request.get_json()
	message = BankAccount.add_bank_account(data['username'], data['bank_name'], data['account_number'], data['balance'])
	return message

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	message = Transaction.add_transaction(data['username'], data['amount'], data['category'], data['date'])
	return message

if __name__ == '__main__':
	app.run(debug=True)
