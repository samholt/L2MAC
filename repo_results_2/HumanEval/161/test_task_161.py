import pytest
from task_161 import solve

def test_solve():
	assert solve('1234') == '4321'
	assert solve('ab') == 'AB'
	assert solve('#a@C') == '#A@c'
	assert solve('') == ''
	assert solve('A') == 'a'
	assert solve('1') == '1'
	assert solve('#') == '#'
	assert solve('a1B#') == 'A1b#'
	assert solve('A1b#') == 'a1B#'
