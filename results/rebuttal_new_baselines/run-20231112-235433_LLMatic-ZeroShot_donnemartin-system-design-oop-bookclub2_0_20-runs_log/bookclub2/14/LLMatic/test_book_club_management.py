import pytest
from app import app, DATABASE, User, BookClub

# Test data
test_user = User('test_user', 'test_password', 'test_email')
DATABASE['users'][test_user.username] = test_user
test_book_club = BookClub('test_book_club', 'public', test_user)

# Test creating book club
def test_create_book_club():
	with app.test_client() as client:
		response = client.post('/create_book_club', json={'name': 'test_book_club', 'privacy': 'public', 'admin': 'test_user'})
		assert response.data == b'Book club created successfully!'
		assert 'test_book_club' in DATABASE['book_clubs']

# Test joining book club
def test_join_book_club():
	with app.test_client() as client:
		response = client.post('/join_book_club', json={'username': 'test_user', 'book_club': 'test_book_club'})
		assert response.data == b'Joined book club successfully!'
		assert test_user.username in [user.username for user in DATABASE['book_clubs']['test_book_club'].members]
