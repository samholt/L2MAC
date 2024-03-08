from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if username in users:
		return {'error': 'username already in use'}, 400
	users[username] = password
	return {'message': 'User created'}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if users.get(username) != password:
		return {'error': 'Invalid username or password'}, 400
	access_token = create_access_token(identity=username)
	return {'access_token': access_token}, 200

@app.route('/protected', methods=['GET'])
@jwt_required

def protected():
	return {'message': 'Access granted'}, 200

if __name__ == '__main__':
	app.run(debug=True)
