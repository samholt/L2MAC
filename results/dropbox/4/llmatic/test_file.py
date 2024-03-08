import pytest
from file import File


def test_file():
	file = File('file_name', 'file_size', 'file_type', 'file_content')
	assert file.name == 'file_name'
	assert file.size == 'file_size'
	assert file.type == 'file_type'
	assert file.content == 'file_content'

	file.write_content('new_content')
	assert file.read_content() == 'new_content'
