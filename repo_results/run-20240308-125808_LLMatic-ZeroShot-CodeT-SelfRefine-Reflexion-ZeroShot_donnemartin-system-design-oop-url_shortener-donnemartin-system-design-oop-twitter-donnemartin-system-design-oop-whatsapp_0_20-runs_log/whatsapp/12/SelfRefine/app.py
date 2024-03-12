from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
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
	user = User(**data)
	user.set_password(data['password'])
	try:
		db.session.add(user)
		db.session.commit()
		return jsonify({'message': 'User registered successfully'}), 201
	except IntegrityError:
		return jsonify({'message': 'Email already in use'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = User.query.filter_by(email=email).first()
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
