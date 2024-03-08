import pytest
from thread import Thread

def test_thread_creation():
	thread = Thread(1, 'Test Thread')
	assert thread.id == 1
	assert thread.title == 'Test Thread'
	assert thread.comments == []

def test_add_comment():
	thread = Thread(1, 'Test Thread')
	thread.add_comment('Test Comment')
	assert thread.comments == ['Test Comment']

def test_remove_comment():
	thread = Thread(1, 'Test Thread')
	thread.add_comment('Test Comment')
	thread.remove_comment('Test Comment')
	assert thread.comments == []

def test_get_info():
	thread = Thread(1, 'Test Thread')
	thread.add_comment('Test Comment')
	info = thread.get_info()
	assert info == {'id': 1, 'title': 'Test Thread', 'comments': ['Test Comment']}
