from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	new_user = User(username=data['username'], email=data['email'], password=hashed_password)
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data['username']).first()
	if not user or not check_password_hash(user.password, data['password']):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = create_access_token(identity=user.username)
	return jsonify({'token': token}), 200


if __name__ == '__main__':
	app.run(debug=True)
