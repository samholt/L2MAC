import pytest
import app

# Test user registration
def test_register():
	response = app.register({'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response == 'User registered successfully!'

# Test user login
def test_login():
	response = app.login({'username': 'test', 'password': 'test'})
	assert response == 'Login successful!'

# Test user follow
def test_follow_user():
	app.register({'username': 'test2', 'password': 'test2', 'email': 'test2@test.com'})
	response = app.follow_user({'username': 'test', 'user_to_follow': 'test2'})
	assert response == 'User followed successfully!'
	assert 'test2' in [user.username for user in app.DATABASE['users']['test'].following]

# Test add to reading list
def test_add_to_reading_list():
	app.DATABASE['books']['book1'] = 'Book 1'
	response = app.add_to_reading_list({'username': 'test', 'book': 'book1'})
	assert response == 'Book added to reading list successfully!'
	assert 'book1' in app.DATABASE['users']['test'].reading_list

# Test add recommendation
def test_add_recommendation():
	app.DATABASE['books']['book2'] = 'Book 2'
	response = app.add_recommendation({'username': 'test', 'book': 'book2'})
	assert response == 'Book recommended successfully!'
	assert 'book2' in app.DATABASE['users']['test'].recommendations
