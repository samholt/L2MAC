import pytest
from forum import Forum

def test_create_forum():
	forum = Forum(None, None)
	forum.create_forum('1', 'Book Club 1')
	assert forum.id == '1'
	assert forum.book_club == 'Book Club 1'
	assert forum.threads == []

def test_add_thread():
	forum = Forum('1', 'Book Club 1')
	forum.add_thread('Thread 1')
	assert forum.threads == ['Thread 1']

def test_update_forum():
	forum = Forum('1', 'Book Club 1')
	forum.update_forum(id='2', book_club='Book Club 2')
	assert forum.id == '2'
	assert forum.book_club == 'Book Club 2'
