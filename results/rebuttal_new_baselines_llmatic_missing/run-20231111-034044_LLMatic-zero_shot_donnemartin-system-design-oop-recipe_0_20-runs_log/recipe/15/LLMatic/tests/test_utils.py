import pytest
from utils import validate_user_input, handle_error, format_response

def test_validate_user_input():
	valid_input = {'name': 'John Doe', 'email': 'john.doe@example.com'}
	invalid_input = {'name': 'John Doe'}
	assert validate_user_input(valid_input) == True
	assert validate_user_input(invalid_input) == False

def test_handle_error():
	error = Exception('Test error')
	assert handle_error(error) == {'status': 'error', 'message': 'Test error'}

def test_format_response():
	data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
	assert format_response(data) == {'status': 'success', 'data': data}
