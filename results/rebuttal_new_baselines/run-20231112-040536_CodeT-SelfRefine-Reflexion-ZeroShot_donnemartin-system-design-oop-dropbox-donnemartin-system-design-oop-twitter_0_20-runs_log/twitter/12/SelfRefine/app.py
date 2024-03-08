from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from user import User, users_db

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if username in users_db:
		return jsonify({'msg': 'Username already exists'}), 400
	new_user = User(username, email, password)
	users_db[username] = new_user
	return jsonify({'msg': 'User created'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users_db.get(username)
	if not user or not user.check_password(password):
		return jsonify({'msg': 'Bad username or password'}), 401
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

if __name__ == '__main__':
	app.run(debug=True)
