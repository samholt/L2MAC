import pytest
from task_111 import histogram

def test_histogram():
	assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
	assert histogram('a b b a') == {'a': 2, 'b': 2}
	assert histogram('a b c a b') == {'a': 2, 'b': 2}
	assert histogram('b b b b a') == {'b': 4}
	assert histogram('') == {}

