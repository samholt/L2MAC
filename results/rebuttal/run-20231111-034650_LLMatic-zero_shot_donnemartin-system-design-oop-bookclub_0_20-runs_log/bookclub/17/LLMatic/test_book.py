import pytest
from book import Book

def test_book():
	book = Book(1, 'Test Title', 'Test Author', 'Test Description')
	assert book.get_data() == {'id': 1, 'title': 'Test Title', 'author': 'Test Author', 'description': 'Test Description', 'votes': 0}
	book.suggest('New Title', 'New Author', 'New Description')
	assert book.get_data() == {'id': 1, 'title': 'New Title', 'author': 'New Author', 'description': 'New Description', 'votes': 0}
	book.update_data('Updated Title', 'Updated Author', 'Updated Description')
	assert book.get_data() == {'id': 1, 'title': 'Updated Title', 'author': 'Updated Author', 'description': 'Updated Description', 'votes': 0}
	book.delete()
	assert book.get_data() == {'id': None, 'title': None, 'author': None, 'description': None, 'votes': 0}
