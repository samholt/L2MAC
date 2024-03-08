from flask import Flask, request

app = Flask(__name__)

# Mock database
vendors = {}

@app.route('/connect_vendor', methods=['POST'])
def connect_vendor():
	vendor_id = request.json['vendor_id']
	vendors[vendor_id] = request.json
	return {'status': 'Vendor connected'}, 200

@app.route('/view_vendor', methods=['GET'])
def view_vendor():
	vendor_id = request.args.get('vendor_id')
	if vendor_id in vendors:
		return vendors[vendor_id]
	else:
		return {'error': 'Vendor not found'}, 404

@app.route('/compare_vendors', methods=['GET'])
def compare_vendors():
	vendor_ids = request.args.getlist('vendor_ids')
	return {vendor_id: vendors.get(vendor_id, 'Vendor not found') for vendor_id in vendor_ids}

@app.route('/message_vendor', methods=['POST'])
def message_vendor():
	vendor_id = request.json['vendor_id']
	message = request.json['message']
	if vendor_id in vendors:
		vendors[vendor_id]['messages'].append(message)
		return {'status': 'Message sent'}, 200
	else:
		return {'error': 'Vendor not found'}, 404
