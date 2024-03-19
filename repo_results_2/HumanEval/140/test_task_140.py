import pytest
from task_140 import fix_spaces

def test_fix_spaces():
	assert fix_spaces('Example') == 'Example'
	assert fix_spaces('Example 1') == 'Example_1'
	assert fix_spaces(' Example 2') == '_Example_2'
	assert fix_spaces(' Example   3') == '_Example-3'

