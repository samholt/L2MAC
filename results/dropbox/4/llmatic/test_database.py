import pytest
from database import Database


def test_database():
	db = Database('test.db')

	record = {'name': 'file_name', 'size': 'file_size', 'type': 'file_type', 'content': 'file_content'}
	db.create_record('files', record)
	assert db.read_record('files', 1) == record

	record['name'] = 'new_file_name'
	db.update_record('files', 1, record)
	assert db.read_record('files', 1)['name'] == 'new_file_name'

	db.delete_record('files', 1)
	assert db.read_record('files', 1) is None

