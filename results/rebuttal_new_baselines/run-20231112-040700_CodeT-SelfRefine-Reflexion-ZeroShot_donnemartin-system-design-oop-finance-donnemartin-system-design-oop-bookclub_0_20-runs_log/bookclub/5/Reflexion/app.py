from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
requests = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: list

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], data['is_private'], [])
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	user_name = data['user_name']
	if clubs[club_name].is_private:
		requests[user_name] = club_name
		return jsonify({'message': 'Request to join club sent'}), 200
	else:
		clubs[club_name].members.append(user_name)
		return jsonify({'message': 'Joined club successfully'}), 200

@app.route('/manage_request', methods=['POST'])
def manage_request():
	data = request.get_json()
	user_name = data['user_name']
	club_name = data['club_name']
	action = data['action']
	if action == 'accept':
		clubs[club_name].members.append(user_name)
		requests.pop(user_name, None)
		return jsonify({'message': 'Request accepted'}), 200
	elif action == 'reject':
		requests.pop(user_name, None)
		return jsonify({'message': 'Request rejected'}), 200

if __name__ == '__main__':
	app.run(debug=True)
