from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
	new_user = User(username=username, password=hashed_password)
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'registered successfully'}), 200


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User.query.filter_by(username=username).first()
	if not user or not check_password_hash(user.password, password):
		return jsonify({'message': 'Invalid username or password'}), 401
	access_token = create_access_token(identity=username)
	return jsonify({'access_token': access_token}), 200


if __name__ == '__main__':
	app.run(debug=True)
