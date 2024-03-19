import pytest
from task_141 import file_name_check

def test_file_name_check():
	assert file_name_check('example.txt') == 'Yes'
	assert file_name_check('1example.dll') == 'No'
	assert file_name_check('example1.txt') == 'Yes'
	assert file_name_check('example12.txt') == 'Yes'
	assert file_name_check('example123.txt') == 'Yes'
	assert file_name_check('example1234.txt') == 'No'
	assert file_name_check('example..txt') == 'No'
	assert file_name_check('.txt') == 'No'
	assert file_name_check('example.doc') == 'No'
