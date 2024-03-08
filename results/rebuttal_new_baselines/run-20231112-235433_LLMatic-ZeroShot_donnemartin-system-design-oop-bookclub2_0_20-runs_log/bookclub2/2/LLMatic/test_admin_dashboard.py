import pytest
from admin_dashboard import AdminDashboard

def test_admin_dashboard():
	ad = AdminDashboard(1)
	ad.create_dashboard(2)
	assert ad.id == 2

	ad.add_user('user1')
	assert 'user1' in ad.users

	ad.remove_user('user1')
	assert 'user1' not in ad.users

	ad.add_book_club('book_club1')
	assert 'book_club1' in ad.book_clubs

	ad.remove_book_club('book_club1')
	assert 'book_club1' not in ad.book_clubs

	ad.add_book('book1')
	assert 'book1' in ad.books

	ad.remove_book('book1')
	assert 'book1' not in ad.books

	info = ad.get_info()
	assert info == {'id': 2, 'users': [], 'book_clubs': [], 'books': []}
