import pytest
from search import Search
from user import User, UserDatabase


def test_search_users():
	users_db = UserDatabase()
	users_db.register('1', 'test1@example.com', 'test1', 'password1', False)
	users_db.register('2', 'test2@example.com', 'test2', 'password2', False)
	users_db.register('3', 'test3@example.com', 'test3', 'password3', False)
	search = Search(users_db, {})
	assert search.search_users('test') == ['test1', 'test2', 'test3']
	assert search.search_users('test1') == ['test1']
	assert search.search_users('nonexistent') == []

