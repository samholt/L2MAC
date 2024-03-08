import pytest
import app

# Test User class

def test_user_authenticate():
	user = app.User('test', 'password')
	assert user.authenticate('password') == True
	assert user.authenticate('wrong_password') == False

def test_user_update_profile():
	user = app.User('test', 'password')
	user.update_profile('new_password')
	assert user.authenticate('new_password') == True

def test_user_follow_user():
	user1 = app.User('test1', 'password')
	user2 = app.User('test2', 'password')
	user1.follow_user(user2)
	assert user2 in user1.following

def test_user_get_info():
	user = app.User('test', 'password')
	info = user.get_info()
	assert info['username'] == 'test'
	assert info['password'] == 'password'
	assert info['following'] == []

def test_user_send_notification():
	user = app.User('test', 'password')
	assert user.send_notification('Notification') == 'Notification sent'

def test_user_customize_notifications():
	user = app.User('test', 'password')
	assert user.customize_notifications('Settings') == 'Notifications customized'

# Test RecommendationEngine class

def test_recommendation_engine_generate_get_recommendations():
	engine = app.RecommendationEngine()
	user = app.User('test', 'password')
	engine.generate_recommendations(user)
	recommendations = engine.get_recommendations(user)
	assert recommendations == ['Book1', 'Book2', 'Book3']

# Test Admin class

def test_admin_manage_book_clubs():
	admin = app.Admin('admin', 'password')
	assert admin.manage_book_clubs('create', 'Book Club') == 'Book club managed successfully'

def test_admin_manage_user_accounts():
	admin = app.Admin('admin', 'password')
	assert admin.manage_user_accounts('delete', 'User') == 'User account managed successfully'

def test_admin_remove_inappropriate_content():
	admin = app.Admin('admin', 'password')
	assert admin.remove_inappropriate_content('Content') == 'Inappropriate content removed successfully'

def test_admin_get_analytics():
	admin = app.Admin('admin', 'password')
	assert admin.get_analytics() == 'Analytics retrieved successfully'

