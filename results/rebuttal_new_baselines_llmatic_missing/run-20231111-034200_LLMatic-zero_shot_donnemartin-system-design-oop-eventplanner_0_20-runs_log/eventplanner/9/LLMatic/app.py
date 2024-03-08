from flask import Flask, request, jsonify
import event_management
from reporting import reporting
from security import hash_password, check_password, generate_auth_token, verify_auth_token

app = Flask(__name__)

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	event_management.create_event(data)
	return jsonify({'message': 'Event created'}), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event_management.update_event(event_id, data)
	return jsonify({'message': 'Event updated'}), 200

@app.route('/events', methods=['GET'])
def get_events():
	return jsonify(event_management.get_events()), 200

@app.route('/report/<int:event_id>', methods=['POST'])
def generate_report(event_id):
	data = request.get_json()
	reporting.generate_report(event_id, data)
	return jsonify({'message': 'Report generated'}), 201

@app.route('/report/<int:event_id>', methods=['GET'])
def get_report(event_id):
	return jsonify(reporting.get_report(event_id)), 200

@app.route('/feedback/<int:event_id>', methods=['POST'])
def collect_feedback(event_id):
	data = request.get_json()
	reporting.collect_feedback(event_id, data)
	return jsonify({'message': 'Feedback collected'}), 201

@app.route('/feedback/<int:event_id>', methods=['GET'])
def get_feedback(event_id):
	return jsonify(reporting.get_feedback(event_id)), 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	password_hash = hash_password(data['password'])
	user_id = event_management.create_user(data['username'], password_hash)
	token = generate_auth_token(user_id)
	return jsonify({'token': token}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = event_management.get_user(data['username'])
	if user and check_password(user['password_hash'], data['password']):
		token = generate_auth_token(user['id'])
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/payment', methods=['POST'])
def make_payment():
	data = request.get_json()
	# Mock payment gateway integration
	if data['amount'] > 0:
		return jsonify({'message': 'Payment successful'}), 200
	return jsonify({'message': 'Payment failed'}), 400

if __name__ == '__main__':
	app.run(debug=True)
