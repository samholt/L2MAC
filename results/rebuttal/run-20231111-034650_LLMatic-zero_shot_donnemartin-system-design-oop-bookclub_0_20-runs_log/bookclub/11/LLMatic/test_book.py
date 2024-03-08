import pytest
from book import Book


def test_book():
	book = Book()
	assert book.suggest_book('Dune', 'Frank Herbert') == 'Book suggested successfully'
	assert book.suggest_book('Dune', 'Frank Herbert') == 'Book already suggested'
	assert book.vote_book('Dune') == 'Vote added successfully'
	assert book.add_review('Dune', 'Great book!') == 'Review added successfully'
	assert book.vote_book('Nonexistent') == 'Book not found'
	assert book.add_review('Nonexistent', 'Great book!') == 'Book not found'
