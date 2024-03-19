from task_4 import mean_absolute_deviation
import pytest

def test_mean_absolute_deviation():
	assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
	assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0
	assert mean_absolute_deviation([1.0, -1.0, 1.0, -1.0]) == 1.0
	assert mean_absolute_deviation([1.0]) == 0.0
	with pytest.raises(ZeroDivisionError):
		mean_absolute_deviation([])
