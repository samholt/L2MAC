import pytest
from app import app
from models import db, User, BookClub, Meeting
from datetime import datetime

def setup_module(module):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	with app.app_context():
		db.create_all()

def teardown_module(module):
	with app.app_context():
		db.drop_all()

def test_schedule_meeting():
	with app.app_context():
		with app.test_client() as client:
			user = User(username='test', email='test@test.com')
			club = BookClub(name='test club', creator=user)
			db.session.add(user)
			db.session.add(club)
			db.session.commit()
			response = client.post('/schedule_meeting', json={'user_id': user.id, 'club_id': club.id, 'date': '2022-12-31', 'time': '12:00:00', 'location': 'Test Location'})
			assert response.status_code == 200
			assert response.get_json()['message'] == 'Meeting scheduled successfully'

def test_send_reminders():
	with app.app_context():
		with app.test_client() as client:
			user = User.query.filter_by(username='test').first()
			club = BookClub.query.filter_by(name='test club').first()
			response = client.get('/send_reminders', json={'user_id': user.id, 'club_id': club.id})
			assert response.status_code == 200
			assert response.get_json()['message'] == 'Reminders sent successfully'
