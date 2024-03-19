import pytest
from task_117 import select_words

def test_select_words():
	assert select_words('Mary had a little lamb', 4) == ['little']
	assert select_words('Mary had a little lamb', 3) == ['Mary', 'lamb']
	assert select_words('simple white space', 2) == []
	assert select_words('Hello world', 4) == ['world']
	assert select_words('Uncle sam', 3) == ['Uncle']
	assert select_words('', 1) == []
	assert select_words('a', 1) == []
	assert select_words('b', 1) == ['b']
	assert select_words('ab', 1) == ['ab']
	assert select_words('ba', 1) == ['ba']
	assert select_words('abc', 1) == []
	assert select_words('bca', 1) == []
	assert select_words('cab', 1) == []
	assert select_words('abc abc', 1) == []
	assert select_words('abc abc', 2) == ['abc', 'abc']
	assert select_words('abc abc', 3) == []
