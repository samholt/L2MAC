from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database Models

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(50))
	date = db.Column(db.String(50))
	time = db.Column(db.String(50))
	theme = db.Column(db.String(50))
	color_scheme = db.Column(db.String(50))

@app.route('/create_event', methods=['POST'])
def create_event():
	data = request.get_json()
	event = Event(**data)
	db.session.add(event)
	db.session.commit()
	return jsonify({'message': 'Event created successfully'}), 201

@app.route('/update_event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	data = request.get_json()
	event = Event.query.get(event_id)
	if not event:
		return jsonify({'message': 'Event not found'}), 404
	event.type = data.get('type', event.type)
	event.date = data.get('date', event.date)
	event.time = data.get('time', event.time)
	event.theme = data.get('theme', event.theme)
	event.color_scheme = data.get('color_scheme', event.color_scheme)
	db.session.commit()
	return jsonify({'message': 'Event updated successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
