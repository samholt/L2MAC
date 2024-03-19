import pytest
from task_84 import solve

def test_solve():
	assert solve(1000) == '1'
	assert solve(150) == '110'
	assert solve(147) == '1100'
