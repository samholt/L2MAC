import pytest
from book_selection import BookSelection


def test_suggest_book():
	book_selection = BookSelection()
	books = book_selection.suggest_book('1', 'user1')
	assert books == {'1': {'suggested_by': 'user1', 'votes': 0}}


def test_vote_for_book():
	book_selection = BookSelection()
	book_selection.suggest_book('1', 'user1')
	books, votes = book_selection.vote_for_book('1', 'user2')
	assert books == {'1': {'suggested_by': 'user1', 'votes': 1}}
	assert votes == {'1': ['user2']}


def test_get_book_data():
	book_selection = BookSelection()
	book_data = book_selection.get_book_data('1')
	assert book_data == {'title': 'Book 1', 'author': 'Author 1'}

