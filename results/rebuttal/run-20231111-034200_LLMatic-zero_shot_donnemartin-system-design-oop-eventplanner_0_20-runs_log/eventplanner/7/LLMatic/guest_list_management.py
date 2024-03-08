from flask import Flask, request

app = Flask(__name__)

guest_lists = {}

@app.route('/create_guest_list', methods=['POST'])
def create_guest_list():
	guest_list_name = request.json['guest_list_name']
	guest_lists[guest_list_name] = []
	return {'status': 'Guest list created.'}, 200

@app.route('/add_guest', methods=['POST'])
def add_guest():
	guest_list_name = request.json['guest_list_name']
	guest = request.json['guest']
	guest_lists[guest_list_name].append(guest)
	return {'status': 'Guest added.'}, 200

@app.route('/get_guest_list', methods=['GET'])
def get_guest_list():
	guest_list_name = request.args.get('guest_list_name')
	return {'guest_list': guest_lists[guest_list_name]}, 200

@app.route('/rsvp', methods=['POST'])
def rsvp():
	guest_list_name = request.json['guest_list_name']
	guest = request.json['guest']
	status = request.json['status']
	for g in guest_lists[guest_list_name]:
		if g['name'] == guest:
			g['rsvp'] = status
	return {'status': 'RSVP updated.'}, 200
