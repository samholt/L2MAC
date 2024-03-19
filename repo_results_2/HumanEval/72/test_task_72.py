import pytest
from task_72 import will_it_fly

def test_will_it_fly():
	assert will_it_fly([1, 2], 5) == False, 'Test Case 1 Failed'
	assert will_it_fly([3, 2, 3], 1) == False, 'Test Case 2 Failed'
	assert will_it_fly([3, 2, 3], 9) == True, 'Test Case 3 Failed'
	assert will_it_fly([3], 5) == True, 'Test Case 4 Failed'
	assert will_it_fly([1, 2, 1], 4) == True, 'Test Case 5 Failed'
	assert will_it_fly([1, 2, 3, 2, 1], 10) == True, 'Test Case 6 Failed'
	assert will_it_fly([1, 2, 3, 4, 5], 15) == False, 'Test Case 7 Failed'
	print('All test cases pass')

if __name__ == '__main__':
	pytest.main()
