from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/venues', methods=['GET'])
def get_venues():
	return {'venues': db.get_all('venues')}

@app.route('/venues', methods=['POST'])
def add_venue():
	data = request.get_json()
	db.insert('venues', data)
	return {'message': 'Venue added successfully'}, 201

@app.route('/venues/<int:id>', methods=['PUT'])
def book_venue(id):
	data = request.get_json()
	db.update('venues', id, data)
	return {'message': 'Venue booked successfully'}, 200
