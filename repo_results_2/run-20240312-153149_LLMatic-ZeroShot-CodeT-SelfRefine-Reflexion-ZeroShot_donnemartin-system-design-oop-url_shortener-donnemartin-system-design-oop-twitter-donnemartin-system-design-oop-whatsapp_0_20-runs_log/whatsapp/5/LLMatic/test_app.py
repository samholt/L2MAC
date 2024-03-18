import pytest
from app import app

@pytest.mark.parametrize('email, password, expected_message', [('test@test.com', 'password', 'User signed up successfully')])
def test_signup(email, password, expected_message):
	with app.test_client() as client:
		response = client.post('/signup', json={'email': email, 'password': password})
		assert response.get_json()['message'] == expected_message

# Add more tests for the other routes here
