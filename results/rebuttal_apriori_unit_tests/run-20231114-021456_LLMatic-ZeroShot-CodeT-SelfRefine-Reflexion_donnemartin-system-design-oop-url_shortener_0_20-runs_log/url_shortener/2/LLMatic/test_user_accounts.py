import pytest
from views import register, login, logout
from database import USERS, SESSIONS


def test_register():
	response = register({'username': 'test', 'password': 'test'})
	assert response == 'User registered successfully'
	assert 'test' in USERS


def test_login():
	response = login({'username': 'test', 'password': 'test'})
	assert response == 'User logged in successfully'
	assert 'test' in SESSIONS


def test_logout():
	response = logout({'username': 'test'})
	assert response == 'User logged out successfully'
	assert 'test' not in SESSIONS
