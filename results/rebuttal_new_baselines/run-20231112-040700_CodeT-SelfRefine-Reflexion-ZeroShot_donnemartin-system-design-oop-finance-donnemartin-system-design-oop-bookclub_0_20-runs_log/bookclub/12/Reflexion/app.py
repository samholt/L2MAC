from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
