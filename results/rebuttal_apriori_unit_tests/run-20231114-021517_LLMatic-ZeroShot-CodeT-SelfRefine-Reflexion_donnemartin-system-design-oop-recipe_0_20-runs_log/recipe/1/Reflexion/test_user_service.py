import pytest
from models.user import User
from services.user_service import UserService

def test_create_user():
	user = User(id='1', username='test', password='test', favorite_recipes=[], followed_users=[])
	UserService.create_user(user)
	assert UserService.get_user('1') == user

def test_update_user():
	user = User(id='1', username='test_updated', password='test', favorite_recipes=[], followed_users=[])
	UserService.update_user(user)
	assert UserService.get_user('1') == user

def test_delete_user():
	UserService.delete_user('1')
	assert UserService.get_user('1') is None
