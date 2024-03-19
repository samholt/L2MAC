import pytest
from task_89 import encrypt

def test_encrypt():
	assert encrypt('hi') == 'lm'
	assert encrypt('asdfghjkl') == 'ewhjklnop'
	assert encrypt('gf') == 'kj'
	assert encrypt('et') == 'ix'
	assert encrypt('') == ''
	assert encrypt('123') == '123'
	assert encrypt('ABC') == 'ABC'
	assert encrypt('a1b2c3') == 'e1f2g3'

