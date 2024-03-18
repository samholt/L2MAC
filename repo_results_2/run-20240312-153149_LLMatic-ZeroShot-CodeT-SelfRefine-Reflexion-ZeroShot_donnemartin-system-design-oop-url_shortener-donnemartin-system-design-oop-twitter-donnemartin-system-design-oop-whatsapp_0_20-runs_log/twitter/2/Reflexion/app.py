from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	password_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
	new_user = User(username=data['username'], email=data['email'], password=password_hash)
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data['username']).first()
	if user and bcrypt.check_password_hash(user.password, data['password']):
		access_token = create_access_token(identity={'username': user.username})
		return jsonify(access_token=access_token), 200
	return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
	app.run(debug=True)
