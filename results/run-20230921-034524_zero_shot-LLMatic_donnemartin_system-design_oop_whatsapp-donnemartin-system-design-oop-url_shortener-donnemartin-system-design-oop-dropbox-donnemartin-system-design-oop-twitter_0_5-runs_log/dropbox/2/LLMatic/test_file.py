import pytest
from file import File


def test_file_creation():
	file = File('test', 100, 'content')
	assert file.name == 'test'
	assert file.size == 100
	assert file.content == 'content'
	assert file.permissions == []


def test_add_permission():
	file = File('test', 100, 'content')
	file.add_permission('read')
	assert 'read' in file.permissions


def test_remove_permission():
	file = File('test', 100, 'content')
	file.add_permission('read')
	file.remove_permission('read')
	assert 'read' not in file.permissions
