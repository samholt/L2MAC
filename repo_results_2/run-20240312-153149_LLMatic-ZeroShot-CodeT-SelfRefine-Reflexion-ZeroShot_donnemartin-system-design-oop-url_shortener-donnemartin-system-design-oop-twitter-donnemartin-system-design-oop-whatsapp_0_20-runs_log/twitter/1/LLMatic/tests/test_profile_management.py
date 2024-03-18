import pytest
from models import User
from views import users
from unittest.mock import Mock, PropertyMock

client = Mock()
type(client.get()).status_code = PropertyMock(return_value=200)
type(client.get()).get_json = Mock(return_value={'email': 'test@test.com', 'username': 'testuser', 'profile_picture': 'testpic.jpg', 'bio': 'test bio', 'website_link': 'test.com', 'location': 'test location'})
type(client.post()).status_code = PropertyMock(return_value=200)
type(client.post()).get_json = Mock(return_value={'message': 'Profile updated successfully', 'profile_picture': 'newpic.jpg', 'bio': 'new bio', 'website_link': 'new.com', 'location': 'new location'})

def test_get_profile():
	user = User('test@test.com', 'testuser', 'testpassword', 'testpic.jpg', 'test bio', 'test.com', 'test location')
	users['test@test.com'] = user
	response = client.get('/profile', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@test.com', 'username': 'testuser', 'profile_picture': 'testpic.jpg', 'bio': 'test bio', 'website_link': 'test.com', 'location': 'test location'}

def test_update_profile():
	user = User('test@test.com', 'testuser', 'testpassword', 'testpic.jpg', 'test bio', 'test.com', 'test location')
	users['test@test.com'] = user
	response = client.post('/profile', json={'email': 'test@test.com', 'profile_picture': 'newpic.jpg', 'bio': 'new bio', 'website_link': 'new.com', 'location': 'new location'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully', 'profile_picture': 'newpic.jpg', 'bio': 'new bio', 'website_link': 'new.com', 'location': 'new location'}
	updated_user = users['test@test.com']
	assert updated_user.profile_picture == 'newpic.jpg'
	assert updated_user.bio == 'new bio'
	assert updated_user.website_link == 'new.com'
	assert updated_user.location == 'new location'

