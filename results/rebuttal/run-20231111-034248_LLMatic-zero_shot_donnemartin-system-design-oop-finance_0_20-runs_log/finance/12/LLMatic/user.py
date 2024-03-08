import hashlib

# Mock database
users_db = {}


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password, email):
	if username in users_db:
		return 'Username already exists'
	else:
		users_db[username] = {'password': hash_password(password), 'email': email, 'bank_accounts': {}}
		return 'User created successfully'


def login(username, password):
	if username in users_db and users_db[username]['password'] == hash_password(password):
		return 'Login successful'
	else:
		return 'Invalid username or password'


def recover_password(username):
	if username in users_db:
		return 'Password recovery email sent'
	else:
		return 'Username does not exist'


def link_bank_account(username, bank_name, account_number, balance):
	if username in users_db:
		users_db[username]['bank_accounts'][account_number] = {'bank_name': bank_name, 'balance': balance, 'transactions': []}
		return 'Bank account linked successfully'
	else:
		return 'Username does not exist'


def import_transactions(username, account_number, transactions):
	if username in users_db and account_number in users_db[username]['bank_accounts']:
		users_db[username]['bank_accounts'][account_number]['transactions'].extend(transactions)
		return 'Transactions imported successfully'
	else:
		return 'Username or account number does not exist'


def update_balance(username, account_number, new_balance):
	if username in users_db and account_number in users_db[username]['bank_accounts']:
		users_db[username]['bank_accounts'][account_number]['balance'] = new_balance
		return 'Balance updated successfully'
	else:
		return 'Username or account number does not exist'


def provide_savings_tips(username):
	if username in users_db:
		# Analyze transactions and provide savings tips
		# This is a mock implementation, in a real application this would involve complex financial analysis
		return 'Save money by reducing your spending on non-essential items'
	else:
		return 'Username does not exist'


def recommend_financial_products(username):
	if username in users_db:
		# Analyze user profile and recommend financial products
		# This is a mock implementation, in a real application this would involve complex financial analysis
		return 'Based on your profile, we recommend investing in a low-risk mutual fund'
	else:
		return 'Username does not exist'
