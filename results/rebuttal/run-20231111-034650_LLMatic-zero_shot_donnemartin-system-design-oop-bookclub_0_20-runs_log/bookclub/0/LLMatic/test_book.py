import pytest
from book import Book

def test_book_creation():
	book = Book('Test Title', 'Test Author')
	assert book.title == 'Test Title'
	assert book.author == 'Test Author'
	assert book.reviews == []

def test_suggest_book():
	book = Book('Test Title', 'Test Author')
	book.suggest_book('Test User', 'Test Book')

def test_vote_for_book():
	book = Book('Test Title', 'Test Author')
	book.vote_for_book('Test User', 'Test Book')
