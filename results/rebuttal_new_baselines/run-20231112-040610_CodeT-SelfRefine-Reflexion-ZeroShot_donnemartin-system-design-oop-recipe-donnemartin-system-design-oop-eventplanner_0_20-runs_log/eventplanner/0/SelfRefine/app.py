from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(50))
	date = db.Column(db.String(50))
	time = db.Column(db.String(50))
	theme = db.Column(db.String(50))
	color_scheme = db.Column(db.String(50))

@app.route('/event', methods=['POST'])
def create_event():
	data = request.get_json()
	event = Event(**data)
	db.session.add(event)
	db.session.commit()
	return jsonify({'message': 'Event created'}), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
	event = Event.query.get(event_id)
	if event:
		data = request.get_json()
		event.type = data.get('type', event.type)
		event.date = data.get('date', event.date)
		event.time = data.get('time', event.time)
		event.theme = data.get('theme', event.theme)
		event.color_scheme = data.get('color_scheme', event.color_scheme)
		db.session.commit()
		return jsonify({'message': 'Event updated'}), 200
	return jsonify({'message': 'Event not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
