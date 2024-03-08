from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	email = db.Column(db.String)
	password = db.Column(db.String)
	profile_picture = db.Column(db.String)
	status_message = db.Column(db.String)
	privacy_settings = db.Column(db.String)

class Message(db.Model):
	id = db.Column(db.String, primary_key=True)
	from_user = db.Column(db.String)
	to_user = db.Column(db.String)
	content = db.Column(db.String)
	read = db.Column(db.Boolean)
	encrypted = db.Column(db.Boolean)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if User.query.get(data['id']):
		return jsonify({'message': 'User already exists'}), 400
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.get(data['id'])
	if user and user.password == data['password']:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	user = User.query.get(data['id'])
	if user:
		user.password = data['new_password']
		db.session.commit()
		return jsonify({'message': 'Password updated successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = User.query.get(data['id'])
	if user:
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		user.status_message = data.get('status_message', user.status_message)
		user.privacy_settings = data.get('privacy_settings', user.privacy_settings)
		db.session.commit()
		return jsonify({'message': 'Profile updated successfully'}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(**data)
	db.session.add(message)
	db.session.commit()
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	message = Message.query.get(data['id'])
	if message:
		message.read = True
		db.session.commit()
		return jsonify({'message': 'Message marked as read'}), 200
	return jsonify({'message': 'Message not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
