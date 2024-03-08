from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/add_security_detail', methods=['POST'])
def add_security_detail():
	data = request.get_json()
	user_id = data['user_id']
	security_detail = data['security_detail']
	db.add_security_detail(user_id, security_detail)
	return {'status': 'success'}, 200

@app.route('/get_security_detail', methods=['GET'])
def get_security_detail():
	user_id = request.args.get('user_id')
	security_detail = db.get_security_detail(user_id)
	if security_detail is None:
		return {'status': 'failure', 'message': 'No security detail found for this user'}, 404
	else:
		return {'status': 'success', 'data': security_detail}, 200
