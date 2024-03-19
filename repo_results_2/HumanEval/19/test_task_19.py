import pytest
from task_19 import sort_numbers

def test_sort_numbers():
	"""Tests the function sort_numbers with various test cases."""
	assert sort_numbers('three one five') == 'one three five'
	assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
	assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
	assert sort_numbers('five five five five five') == 'five five five five five'
	assert sort_numbers('one one two two three three') == 'one one two two three three'
