from flask import Flask, request, jsonify
from dataclasses import dataclass
from marshmallow import Schema, fields, ValidationError

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


class EventSchema(Schema):
	type = fields.Str(required=True)
	date = fields.Date(required=True)
	time = fields.Str(required=True)
	theme = fields.Str(required=True)
	color_scheme = fields.Str(required=True)

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	schema = EventSchema()
	try:
		validated_data = schema.load(data)
	except ValidationError as e:
		return jsonify({'error': str(e)}), 400
	id = len(DB) + 1
	event = Event(id, validated_data['type'], validated_data['date'], validated_data['time'], validated_data['theme'], validated_data['color_scheme'])
	DB[id] = event
	return jsonify({'id': id}), 201

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
	event = DB.get(id)
	if not event:
		return jsonify({'error': 'Event not found'}), 404
	return jsonify({'id': event.id, 'type': event.type, 'date': event.date, 'time': event.time, 'theme': event.theme, 'color_scheme': event.color_scheme}), 200

if __name__ == '__main__':
	app.run(debug=True)
