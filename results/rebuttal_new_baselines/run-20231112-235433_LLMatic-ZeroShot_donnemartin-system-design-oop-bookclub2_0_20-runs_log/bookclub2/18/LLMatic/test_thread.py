import pytest
from thread import Thread

def test_thread_creation():
	thread = Thread('Test Thread', 'Test Author')
	assert thread.title == 'Test Thread'
	assert thread.author == 'Test Author'
	assert thread.comments == []

def test_add_comment():
	thread = Thread('Test Thread', 'Test Author')
	thread.add_comment('Test Comment')
	assert thread.comments == ['Test Comment']
