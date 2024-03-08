from flask import Flask, request, jsonify
from dataclasses import dataclass
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database model
class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(50))
	date = db.Column(db.DateTime)
	time = db.Column(db.Time)
	theme = db.Column(db.String(50))
	color_scheme = db.Column(db.String(50))

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	if 'id' not in data or 'type' not in data or 'date' not in data or 'time' not in data or 'theme' not in data or 'color_scheme' not in data:
		return jsonify({'message': 'Invalid data'}), 400
	data['date'] = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
	data['time'] = datetime.datetime.strptime(data['time'], '%H:%M:%S').time()
	event = Event(**data)
	db.session.add(event)
	db.session.commit()
	return jsonify({'message': 'Event created successfully'}), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	if 'date' in data:
		data['date'] = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
	if 'time' in data:
		data['time'] = datetime.datetime.strptime(data['time'], '%H:%M:%S').time()
	event = Event.query.get(event_id)
	if event:
		event.__dict__.update(data)
		db.session.commit()
		return jsonify({'message': 'Event updated successfully'}), 200
	else:
		return jsonify({'message': 'Event not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
