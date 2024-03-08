from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	profile_picture = db.Column(db.String(120))
	status_message = db.Column(db.String(120))
	privacy_settings = db.Column(db.JSON)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	from_user = db.Column(db.String(120), nullable=False)
	to_user = db.Column(db.String(120), nullable=False)
	message = db.Column(db.String(120), nullable=False)
	read = db.Column(db.Boolean, default=False)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if User.query.filter_by(email=data.get('email')).first():
		return jsonify({'message': 'Email already in use'}), 400
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = User.query.filter_by(email=email, password=password).first()
	if not user:
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if not User.query.filter_by(email=data.get('to_user')).first():
		return jsonify({'message': 'Recipient email not found'}), 400
	message = Message(**data)
	db.session.add(message)
	db.session.commit()
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/read_messages', methods=['GET'])
def read_messages():
	email = request.args.get('email')
	user_messages = Message.query.filter_by(to_user=email).all()
	for message in user_messages:
		message.read = True
	db.session.commit()
	return jsonify({'messages': [message.message for message in user_messages]}), 200

if __name__ == '__main__':
	app.run(debug=True)
