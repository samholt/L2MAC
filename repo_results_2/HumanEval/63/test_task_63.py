import pytest
from task_63 import fibfib

def test_fibfib():
	assert fibfib(0) == 0
	assert fibfib(1) == 0
	assert fibfib(2) == 1
	assert fibfib(3) == 1
	assert fibfib(4) == 2
	assert fibfib(5) == 4
	assert fibfib(6) == 7
	assert fibfib(7) == 13
	assert fibfib(8) == 24
	assert fibfib(9) == 44
	assert fibfib(10) == 81
