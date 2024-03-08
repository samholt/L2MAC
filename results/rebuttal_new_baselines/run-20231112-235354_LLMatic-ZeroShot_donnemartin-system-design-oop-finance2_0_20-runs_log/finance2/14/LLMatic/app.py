from flask import Flask, request, jsonify
from models.user import User
from models.transaction import Transaction
from models.budget import Budget
from models.investment import Investment
from models.alert import Alert

app = Flask(__name__)

user = User('test', 'test@test.com', 'password')
budget = Budget()
investment = Investment(user, 1000, 'Stocks')
alert = Alert(user, 'Low Balance', 100)

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user.create_user(data)
	return jsonify({'message': 'User created'}), 201

@app.route('/authenticate_user', methods=['POST'])
def authenticate_user():
	data = request.get_json()
	if user.authenticate(data['password']):
		user.send_verification_code()
		return jsonify({'message': 'User authenticated, verification code sent'}), 200
	else:
		return jsonify({'message': 'Authentication failed'}), 401

@app.route('/verify_user', methods=['POST'])
def verify_user():
	data = request.get_json()
	if user.name == data['name'] and user.verify(int(data['code'])):
		user.verification_code = None
		return jsonify({'message': 'User verified'}), 200
	else:
		return jsonify({'message': 'Verification failed'}), 401

@app.route('/track_investment_performance', methods=['POST'])
def track_investment_performance():
	data = request.get_json()
	if user.name == data['user']:
		return jsonify(investment.track_performance()), 200
	return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
