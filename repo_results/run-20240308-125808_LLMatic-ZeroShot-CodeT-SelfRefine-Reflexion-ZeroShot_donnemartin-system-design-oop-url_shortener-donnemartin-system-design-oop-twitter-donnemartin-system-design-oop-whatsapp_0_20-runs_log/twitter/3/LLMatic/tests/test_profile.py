import pytest
from flask import json
from models import User, users_db
from views import views
from app import app


def test_update_profile():
	user = User('test@test.com', 'testuser', 'testpass')
	users_db['test@test.com'] = user
	with app.test_client() as c:
		response = c.put('/update-profile', data=json.dumps({'email': 'test@test.com', 'profile_picture': 'newpic.jpg', 'bio': 'new bio', 'website_link': 'newwebsite.com', 'location': 'new location'}), content_type='application/json')
		data = json.loads(response.get_data(as_text=True))
		assert data['message'] == 'Profile updated successfully'
		assert user.profile_picture == 'newpic.jpg'
		assert user.bio == 'new bio'
		assert user.website_link == 'newwebsite.com'
		assert user.location == 'new location'
