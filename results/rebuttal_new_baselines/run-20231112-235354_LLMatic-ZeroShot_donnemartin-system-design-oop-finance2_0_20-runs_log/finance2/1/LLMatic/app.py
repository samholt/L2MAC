from flask import Flask, request, make_response
from models.user import User

app = Flask(__name__)

users_db = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	email = data['email']
	user = User(username, password, email)
	users_db[username] = user
	return 'User registered successfully', 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users_db.get(username)
	if user and user.password == password:
		verification_code = user.generate_verification_code()
		response = make_response('Verification code sent to email', 200)
		response.headers['X-Verification-Code'] = verification_code
		return response
	else:
		return 'Invalid credentials', 401

@app.route('/verify', methods=['POST'])
def verify():
	data = request.get_json()
	username = data['username']
	code = data['code']
	user = users_db.get(username)
	if user and user.verify(code):
		return 'Login successful', 200
	else:
		return 'Invalid verification code', 401

@app.route('/user', methods=['PUT'])
def update_user():
	data = request.get_json()
	username = data['username']
	new_password = data.get('new_password')
	new_email = data.get('new_email')
	user = users_db.get(username)
	if user:
		if new_password:
			user.password = new_password
		if new_email:
			user.email = new_email
		return 'User updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/bank_account', methods=['POST'])
def add_bank_account():
	data = request.get_json()
	username = data['username']
	password = data['password']
	bank_name = data['bank_name']
	account_number = data['account_number']
	balance = data['balance']
	user = users_db.get(username)
	if user and user.password == password:
		user.add_bank_account(bank_name, account_number, balance)
		return 'Bank account added successfully', 201
	else:
		return 'Invalid credentials', 401

@app.route('/bank_account', methods=['PUT'])
def update_bank_account():
	data = request.get_json()
	username = data['username']
	password = data['password']
	account_number = data['account_number']
	new_bank_name = data.get('new_bank_name')
	new_balance = data.get('new_balance')
	user = users_db.get(username)
	if user and user.password == password:
		if user.update_bank_account(account_number, new_bank_name, new_balance):
			return 'Bank account updated successfully', 200
		else:
			return 'Bank account not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/bank_account', methods=['DELETE'])
def delete_bank_account():
	data = request.get_json()
	username = data['username']
	password = data['password']
	account_number = data['account_number']
	user = users_db.get(username)
	if user and user.password == password:
		if user.delete_bank_account(account_number):
			return 'Bank account deleted successfully', 200
		else:
			return 'Bank account not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	username = data['username']
	password = data['password']
	amount = data['amount']
	date = data.get('date')
	category = data['category']
	type = data['type']
	user = users_db.get(username)
	if user and user.password == password:
		user.add_transaction(amount, date, category, type)
		return 'Transaction added successfully', 201
	else:
		return 'Invalid credentials', 401

@app.route('/transaction', methods=['PUT'])
def update_transaction():
	data = request.get_json()
	username = data['username']
	password = data['password']
	transaction_id = data['transaction_id']
	new_amount = data.get('new_amount')
	new_date = data.get('new_date')
	new_category = data.get('new_category')
	new_type = data.get('new_type')
	user = users_db.get(username)
	if user and user.password == password:
		if user.update_transaction(transaction_id, new_amount, new_date, new_category, new_type):
			return 'Transaction updated successfully', 200
		else:
			return 'Transaction not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/transaction', methods=['DELETE'])
def delete_transaction():
	data = request.get_json()
	username = data['username']
	password = data['password']
	transaction_id = data['transaction_id']
	user = users_db.get(username)
	if user and user.password == password:
		if user.delete_transaction(transaction_id):
			return 'Transaction deleted successfully', 200
		else:
			return 'Transaction not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/transaction_history', methods=['GET'])
def get_transaction_history():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users_db.get(username)
	if user and user.password == password:
		transaction_history = user.get_transaction_history()
		return {'transaction_history': transaction_history}, 200
	else:
		return 'Invalid credentials', 401

@app.route('/budget', methods=['POST'])
def add_budget():
	data = request.get_json()
	username = data['username']
	password = data['password']
	amount = data['amount']
	month = data['month']
	user = users_db.get(username)
	if user and user.password == password:
		user.add_budget(amount, month)
		return 'Budget added successfully', 201
	else:
		return 'Invalid credentials', 401

@app.route('/budget', methods=['PUT'])
def update_budget():
	data = request.get_json()
	username = data['username']
	password = data['password']
	month = data['month']
	new_amount = data.get('new_amount')
	user = users_db.get(username)
	if user and user.password == password:
		if user.update_budget(month, new_amount):
			return 'Budget updated successfully', 200
		else:
			return 'Budget not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/budget', methods=['DELETE'])
def delete_budget():
	data = request.get_json()
	username = data['username']
	password = data['password']
	month = data['month']
	user = users_db.get(username)
	if user and user.password == password:
		if user.delete_budget(month):
			return 'Budget deleted successfully', 200
		else:
			return 'Budget not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/alerts', methods=['GET'])
def get_alerts():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users_db.get(username)
	if user and user.password == password:
		alerts = user.get_alerts()
		return {'alerts': alerts}, 200
	else:
		return 'Invalid credentials', 401

@app.route('/investment', methods=['POST'])
def add_investment():
	data = request.get_json()
	username = data['username']
	password = data['password']
	account_name = data['account_name']
	balance = data['balance']
	asset_allocation = data['asset_allocation']
	user = users_db.get(username)
	if user and user.password == password:
		user.add_investment(account_name, balance, asset_allocation)
		return 'Investment added successfully', 201
	else:
		return 'Invalid credentials', 401

@app.route('/investment', methods=['PUT'])
def update_investment():
	data = request.get_json()
	username = data['username']
	password = data['password']
	account_name = data['account_name']
	new_balance = data.get('new_balance')
	new_asset_allocation = data.get('new_asset_allocation')
	user = users_db.get(username)
	if user and user.password == password:
		if user.update_investment(account_name, new_balance, new_asset_allocation):
			return 'Investment updated successfully', 200
		else:
			return 'Investment not found', 404
	else:
		return 'Invalid credentials', 401

@app.route('/investment', methods=['DELETE'])
def delete_investment():
	data = request.get_json()
	username = data['username']
	password = data['password']
	account_name = data['account_name']
	user = users_db.get(username)
	if user and user.password == password:
		if user.delete_investment(account_name):
			return 'Investment deleted successfully', 200
		else:
			return 'Investment not found', 404
	else:
		return 'Invalid credentials', 401

if __name__ == '__main__':
	app.run(debug=True)
