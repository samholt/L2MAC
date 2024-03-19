import pytest
from task_160 import do_algebra

def test_do_algebra():
	assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
	assert do_algebra(['*', '+', '**'], [1, 2, 3, 4]) == 83
	assert do_algebra(['//', '-', '+'], [10, 2, 3, 4]) == 6
