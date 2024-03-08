from flask import Flask, request, jsonify
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/vendors', methods=['POST'])
def add_vendor():
	vendor = request.get_json()
	vendor_id = db.insert('vendors', vendor)
	return jsonify({'id': vendor_id}), 201

@app.route('/vendors', methods=['GET'])
def get_vendors():
	vendors = db.get_all('vendors')
	return jsonify(vendors), 200

@app.route('/vendors/<int:vendor_id>', methods=['GET'])
def get_vendor(vendor_id):
	vendor = db.get('vendors', vendor_id)
	if vendor is None:
		return '', 404
	return jsonify(vendor), 200

@app.route('/vendors/<int:vendor_id>/messages', methods=['POST'])
def send_message(vendor_id):
	message = request.get_json()
	message['vendor_id'] = vendor_id
	message_id = db.insert('messages', message)
	return jsonify({'id': message_id}), 201
