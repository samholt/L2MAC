import pytest
from task_110 import exchange

def test_exchange_1():
	assert exchange([2, 4, 6], [1, 3, 5]) == 'YES'

def test_exchange_2():
	assert exchange([1, 3, 5], [2, 4, 6]) == 'YES'

def test_exchange_3():
	assert exchange([1, 3, 5], [1, 3, 5]) == 'NO'

def test_exchange_4():
	assert exchange([2, 4, 6], [2, 4, 6]) == 'YES'

def test_exchange_5():
	assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == 'YES'

def test_exchange_6():
	assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == 'NO'
