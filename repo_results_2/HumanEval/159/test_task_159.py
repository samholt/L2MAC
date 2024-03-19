import pytest
from task_159 import eat

def test_eat():
	assert eat(5, 6, 10) == [11, 4]
	assert eat(4, 8, 9) == [12, 1]
	assert eat(1, 10, 10) == [11, 0]
	assert eat(2, 11, 5) == [7, 0]

# This function tests the 'eat' function from the 'task_159.py' file.
# It calls the 'eat' function with different sets of parameters and checks if the returned result is as expected.
# For example, if the 'eat' function is called with parameters (5, 6, 10), the expected result is [11, 4].
# If the 'eat' function is called with parameters (4, 8, 9), the expected result is [12, 1].
# If the 'eat' function is called with parameters (1, 10, 10), the expected result is [11, 0].
# If the 'eat' function is called with parameters (2, 11, 5), the expected result is [7, 0].
