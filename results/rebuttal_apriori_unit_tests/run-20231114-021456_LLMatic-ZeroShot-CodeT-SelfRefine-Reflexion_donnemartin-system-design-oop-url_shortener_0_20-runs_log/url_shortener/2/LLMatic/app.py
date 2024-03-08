from flask import Flask, request
from views import register, login, logout

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_route():
	return register(request.json)

@app.route('/login', methods=['POST'])
def login_route():
	return login(request.json)

@app.route('/logout', methods=['POST'])
def logout_route():
	return logout(request.json)

if __name__ == '__main__':
	app.run(debug=True)
