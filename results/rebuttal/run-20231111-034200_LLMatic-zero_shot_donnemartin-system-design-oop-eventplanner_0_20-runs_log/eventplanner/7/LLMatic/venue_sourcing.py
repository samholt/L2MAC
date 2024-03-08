from flask import Flask, request
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/add_venue', methods=['POST'])
def add_venue():
	venue_id = request.json['venue_id']
	venue_details = request.json['venue_details']
	db.add_venue(venue_id, venue_details)
	return {'status': 'success'}, 200

@app.route('/get_venue/<venue_id>', methods=['GET'])
def get_venue(venue_id):
	venue = db.get_venue(venue_id)
	if venue:
		return venue, 200
	else:
		return {'error': 'Venue not found'}, 404

@app.route('/search_venues', methods=['GET'])
def search_venues():
	search_term = request.args.get('search_term')
	venues = db.search_venues(search_term)
	return venues, 200
