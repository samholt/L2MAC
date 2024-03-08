import pytest
from auth import generate_token, decode_token


def test_generate_token():
	token = generate_token('testuser')
	assert isinstance(token, str)


def test_decode_token():
	token = generate_token('testuser')
	decoded_token = decode_token(token)
	assert 'sub' in decoded_token and decoded_token['sub'] == 'testuser'

	invalid_token = 'invalid'
	assert decode_token(invalid_token) == 'Invalid token. Please log in again.'
