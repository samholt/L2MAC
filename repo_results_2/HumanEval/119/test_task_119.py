import pytest
from task_119 import match_parens

def test_match_parens():
	assert match_parens(['()(', ')']) == 'Yes'
	assert match_parens([')', ')']) == 'No'
	assert match_parens(['(', ')']) == 'Yes'
	assert match_parens(['(', '(']) == 'No'
	assert match_parens([')', '(']) == 'No'
	assert match_parens([')(', ')(']) == 'No'
	assert match_parens(['(()', ')']) == 'Yes'
	assert match_parens([')(', '))']) == 'No'
