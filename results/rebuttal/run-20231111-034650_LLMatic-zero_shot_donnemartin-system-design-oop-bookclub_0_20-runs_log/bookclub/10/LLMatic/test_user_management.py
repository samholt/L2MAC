import pytest
import app


def test_create_user():
	user_data = {'id': '1', 'username': 'testuser', 'email': 'testuser@example.com', 'password': 'password', 'interests': ['fiction', 'non-fiction'], 'books': ['book1', 'book2']}
	response = app.create_user(user_data)
	assert response == ({'message': 'User created successfully'}, 201)


def test_get_user():
	response = app.get_user('1')
	assert response == {'id': '1', 'username': 'testuser', 'email': 'testuser@example.com', 'password': 'password', 'interests': ['fiction', 'non-fiction'], 'books': ['book1', 'book2']}


def test_update_user():
	update_data = {'username': 'updateduser', 'email': 'updateduser@example.com', 'password': 'newpassword', 'interests': ['history', 'biography'], 'books': ['book3', 'book4']}
	response = app.update_user('1', update_data)
	assert response == ({'message': 'User updated successfully'})


def test_delete_user():
	response = app.delete_user('1')
	assert response == ({'message': 'User deleted successfully'})


def test_user_profile():
	user_data = {'id': '2', 'username': 'testuser2', 'email': 'testuser2@example.com', 'password': 'password2', 'interests': ['mystery', 'thriller'], 'books': ['book5', 'book6']}
	app.create_user(user_data)
	response = app.get_user('2')
	assert response == {'id': '2', 'username': 'testuser2', 'email': 'testuser2@example.com', 'password': 'password2', 'interests': ['mystery', 'thriller'], 'books': ['book5', 'book6']}
