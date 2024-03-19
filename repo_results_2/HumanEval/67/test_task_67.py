import pytest
from task_67 import fruit_distribution

def test_fruit_distribution():
	assert fruit_distribution("5 apples and 6 oranges", 19) == 8
	assert fruit_distribution("0 apples and 1 oranges",3) == 2
	assert fruit_distribution("2 apples and 3 oranges", 100) == 95
	assert fruit_distribution("100 apples and 1 oranges",120) == 19
	# edge cases
	assert fruit_distribution("0 apples and 0 oranges", 0) == 0
	assert fruit_distribution("10 apples and 10 oranges", 15) == -5
	assert fruit_distribution("0 apples and 0 oranges", 10) == 10
	assert fruit_distribution("5 apples and 0 oranges", 5) == 0
	assert fruit_distribution("0 apples and 5 oranges", 5) == 0
