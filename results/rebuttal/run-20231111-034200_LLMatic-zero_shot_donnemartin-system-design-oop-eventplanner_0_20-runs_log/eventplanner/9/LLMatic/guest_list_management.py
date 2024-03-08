from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/create_guest_list', methods=['POST'])
def create_guest_list():
	data = request.get_json()
	id = db.insert('guest_lists', data)
	return {'message': 'Guest list created successfully', 'id': id}, 201

@app.route('/get_guest_list/<int:id>', methods=['GET'])
def get_guest_list(id):
	guest_list = db.get('guest_lists', id)
	if guest_list:
		return guest_list
	else:
		return {'message': 'Guest list not found'}, 404

@app.route('/update_guest_list/<int:id>', methods=['PUT'])
def update_guest_list(id):
	data = request.get_json()
	if db.update('guest_lists', id, data):
		return {'message': 'Guest list updated successfully'}, 200
	else:
		return {'message': 'Guest list not found'}, 404

@app.route('/delete_guest_list/<int:id>', methods=['DELETE'])
def delete_guest_list(id):
	if db.delete('guest_lists', id):
		return {'message': 'Guest list deleted successfully'}, 200
	else:
		return {'message': 'Guest list not found'}, 404

@app.route('/rsvp/<int:id>', methods=['PUT'])
def rsvp(id):
	data = request.get_json()
	guest_list = db.get('guest_lists', id)
	if guest_list:
		guest_list['rsvp'] = data.get('rsvp')
		if db.update('guest_lists', id, guest_list):
			return {'message': 'RSVP updated successfully'}, 200
	return {'message': 'Guest list not found'}, 404
