from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@dataclass
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(128))
	profile_picture = db.Column(db.String(200))
	status_message = db.Column(db.String(200))
	privacy_settings = db.Column(db.PickleType)
	contacts = db.Column(db.PickleType)
	groups = db.Column(db.PickleType)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if User.query.filter_by(email=data['email']).first() is not None:
		return jsonify({'message': 'Email already in use'}), 400
	user = User(name=data['name'], email=data['email'])
	user.set_password(data['password'])
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and user.check_password(data['password']):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid email or password'}), 401

if __name__ == '__main__':
	app.run(debug=True)
