import pytest
from user_management.routes import mock_db, User
from main import app


def test_profile():
	user = User('Test User', 'test@example.com', 'password')
	mock_db['test@example.com'] = user
	client = app.test_client()
	with client.session_transaction() as session:
		session['user'] = 'test@example.com'
	response = client.get('/profile')
	assert 'Test User' in response.get_data(as_text=True)
	assert 'test@example.com' in response.get_data(as_text=True)
	assert '0 MB' in response.get_data(as_text=True)
	assert '100 MB' in response.get_data(as_text=True)
	response = client.post('/profile', data={'new_password': 'new_password'})
	assert 'Password changed successfully' in response.get_data(as_text=True)
	assert mock_db['test@example.com'].password == 'new_password'
