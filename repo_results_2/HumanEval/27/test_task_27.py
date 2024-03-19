import pytest
from task_27 import flip_case

def test_flip_case():
	assert flip_case('Hello') == 'hELLO'
	assert flip_case('') == ''
	assert flip_case('123') == '123'
	assert flip_case('HELLO') == 'hello'
	assert flip_case('hello') == 'HELLO'
