import pytest
from thread import Thread

def test_thread_creation():
	thread = Thread('1', 'Test Thread', 'Author')
	assert thread.id == '1'
	assert thread.title == 'Test Thread'
	assert thread.author == 'Author'
	assert thread.comments == []

def test_add_comment():
	thread = Thread('1', 'Test Thread', 'Author')
	thread.add_comment('Test Comment')
	assert thread.comments == ['Test Comment']

def test_update_thread():
	thread = Thread('1', 'Test Thread', 'Author')
	thread.update_thread(title='Updated Title', author='Updated Author')
	assert thread.title == 'Updated Title'
	assert thread.author == 'Updated Author'
