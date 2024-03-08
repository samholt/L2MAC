import pytest
from admin_dashboard import AdminDashboard

admin = AdminDashboard()

def test_manage_users():
	assert admin.manage_users('create', name='Test User', email='test@test.com', password='test') == 'User created successfully'
	users = admin.manage_users('view')
	assert len(users) == 1
	assert admin.manage_users('delete', user_id=list(users.keys())[0]) == 'User deleted successfully'
	assert len(admin.manage_users('view')) == 0

def test_manage_book_clubs():
	assert admin.manage_book_clubs('create', name='Test Club', description='This is a test club', privacy='public') == 'Book club created successfully'
	clubs = admin.manage_book_clubs('view')
	assert len(clubs) == 1
	assert admin.manage_book_clubs('delete', club_id=list(clubs.keys())[0]) == 'Book club deleted successfully'
	assert len(admin.manage_book_clubs('view')) == 0

def test_view_analytics():
	analytics = admin.view_analytics()
	assert 'user_engagement' in analytics
	assert 'book_club_engagement' in analytics
	assert 'popular_books' in analytics
