import pytest
from task_86 import anti_shuffle

def test_anti_shuffle():
	assert anti_shuffle('Hi') == 'Hi'
	assert anti_shuffle('hello') == 'ehllo'
	assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'

