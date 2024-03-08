import pytest
from profile import app
from models import db, User


def setup_module():
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
	db.init_app(app)
	db.create_all(app=app)


def teardown_module():
	db.session.remove()
	db.drop_all(app=app)


def test_update_profile():
	with app.test_client() as client:
		response = client.put('/profile', json={
			'profile_picture': 'new_picture.jpg',
			'bio': 'New bio',
			'website_link': 'https://newwebsite.com',
			'location': 'New location',
			'is_private': True
		})
		data = response.get_json()
		assert response.status_code == 200
		assert data['message'] == 'Profile updated successfully'
