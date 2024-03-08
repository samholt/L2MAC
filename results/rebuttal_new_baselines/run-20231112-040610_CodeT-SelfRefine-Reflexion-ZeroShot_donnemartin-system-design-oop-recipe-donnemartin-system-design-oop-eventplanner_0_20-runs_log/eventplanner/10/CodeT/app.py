from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class Event:
	id: int
	type: str
	date: str
	time: str
	theme: str
	color_scheme: str

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	id = len(DB) + 1
	event = Event(id, **data)
	DB[id] = event
	return jsonify(event), 201

@app.route('/event/<int:id>', methods=['PUT'])
def update_event(id):
	data = request.get_json()
	DB[id].__dict__.update(data)
	return jsonify(DB[id]), 200

if __name__ == '__main__':
	app.run(debug=True)
