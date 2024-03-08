import pytest
from forum import Forum

def test_forum():
	forum = Forum(1, 'Test Forum')
	assert forum.get_info() == {'id': 1, 'title': 'Test Forum', 'threads': []}

	forum.add_thread('Test Thread')
	assert forum.get_info() == {'id': 1, 'title': 'Test Forum', 'threads': ['Test Thread']}

	forum.remove_thread('Test Thread')
	assert forum.get_info() == {'id': 1, 'title': 'Test Forum', 'threads': []}
