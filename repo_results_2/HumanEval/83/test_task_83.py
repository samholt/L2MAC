import pytest
from task_83 import starts_one_ends

def test_starts_one_ends():
	# Test edge cases
	assert starts_one_ends(1) == 2
	assert starts_one_ends(2) == 19
	
	# Test random cases
	assert starts_one_ends(3) == 190
	assert starts_one_ends(4) == 1900
	
	# Test invalid input
	with pytest.raises(ValueError):
		starts_one_ends(0)
	with pytest.raises(ValueError):
		starts_one_ends(-1)
	with pytest.raises(ValueError):
		starts_one_ends('a')
