from flask import Flask, request, jsonify
from user_management import UserManagement

app = Flask(__name__)
user_management = UserManagement()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	response = user_management.register(data)
	return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	response = user_management.login(data)
	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)
