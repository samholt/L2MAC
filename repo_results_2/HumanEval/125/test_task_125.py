import pytest
from task_125 import split_words

def test_split_words():
	assert split_words('Hello world!') == ['Hello', 'world!']
	assert split_words('Hello,world!') == ['Hello', 'world!']
	assert split_words('abcdef') == 3
