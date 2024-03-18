from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
jwt = JWTManager(app)

import models
import services

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = services.register_user(data)
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = services.authenticate_user(data)
	if user:
		access_token = create_access_token(identity=user['username'])
		return jsonify(access_token=access_token), 200
	return jsonify(message='Invalid username or password'), 401

@app.route('/profile', methods=['GET', 'PUT'])
@jwt_required

def profile():
	if request.method == 'GET':
		username = get_jwt_identity()
		user = services.get_user(username)
		return jsonify(user), 200
	elif request.method == 'PUT':
		data = request.get_json()
		username = get_jwt_identity()
		user = services.update_user(username, data)
		return jsonify(user), 200

if __name__ == '__main__':
	app.run(debug=True)
