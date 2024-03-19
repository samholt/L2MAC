import pytest
from task_156 import int_to_mini_roman

def test_int_to_mini_roman():
	assert int_to_mini_roman(19) == 'xix'
	assert int_to_mini_roman(152) == 'clii'
	assert int_to_mini_roman(426) == 'cdxxvi'
	assert int_to_mini_roman(1) == 'i'
	assert int_to_mini_roman(1000) == 'm'
	assert int_to_mini_roman(444) == 'cdxliv'
	assert int_to_mini_roman(555) == 'dlv'

	with pytest.raises(ValueError):
		int_to_mini_roman(0)
		int_to_mini_roman(1001)

