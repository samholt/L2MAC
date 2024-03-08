import pytest
from models import User, Book, Admin

@pytest.fixture
def admin():
	return Admin('admin', 'password')

@pytest.fixture
def users():
	return {
		'user1': User('user1', 'user1@email.com', 'password', ['genre1'], [], []),
		'user2': User('user2', 'user2@email.com', 'password', ['genre2'], [], [])
	}

@pytest.fixture
def books():
	return {
		'book1': Book('book1', 'author1', 'genre1'),
		'book2': Book('book2', 'author2', 'genre2')
	}


def test_manage_users(admin, users):
	assert len(admin.manage_users(users)) == 2


def test_manage_books(admin, books):
	assert len(admin.manage_books(books)) == 2


def test_remove_user(admin, users):
	assert admin.remove_user(users, 'user1') == 'User removed successfully'
	assert len(users) == 1


def test_remove_book(admin, books):
	assert admin.remove_book(books, 'book1') == 'Book removed successfully'
	assert len(books) == 1


def test_view_analytics(admin, users):
	users['user1'].read_books.append(Book('book1', 'author1', 'genre1'))
	users['user2'].read_books.append(Book('book1', 'author1', 'genre1'))
	users['user2'].read_books.append(Book('book2', 'author2', 'genre2'))
	analytics = admin.view_analytics(users)
	assert analytics['user_engagement'] == {'user1': 1, 'user2': 2}
	assert analytics['popular_books'] == {'book1': 2, 'book2': 1}
