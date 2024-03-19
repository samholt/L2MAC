import pytest
from task_69 import search

def test_search():
	assert search([4, 1, 2, 2, 3, 1]) == 2
	assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
	assert search([5, 5, 4, 4, 4]) == -1
	assert search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3
	assert search([1]) == 1
	assert search([2, 3, 4, 5, 6, 7]) == -1
