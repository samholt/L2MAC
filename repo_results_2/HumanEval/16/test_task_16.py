import pytest
from task_16 import count_distinct_characters

def test_count_distinct_characters():
	assert count_distinct_characters('xyzXYZ') == 3
	assert count_distinct_characters('Jerry') == 4
	assert count_distinct_characters('') == 0
	assert count_distinct_characters('1234567890') == 10
	assert count_distinct_characters('aAaAaA') == 1
