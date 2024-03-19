import pytest
from task_21 import rescale_to_unit

def test_rescale_to_unit():
	assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
	assert rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
	assert rescale_to_unit([-1.0, 0.0, 1.0]) == [0.0, 0.5, 1.0]
	assert rescale_to_unit([0.0, 0.0, 0.0, 1.0]) == [0.0, 0.0, 0.0, 1.0]
	assert rescale_to_unit([1.0, 1.0, 1.0, 1.0]) == [0.0, 0.0, 0.0, 0.0]
