from task_9 import rolling_max


def test_rolling_max():
	assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
	assert rolling_max([]) == []
	assert rolling_max([5]) == [5]
	assert rolling_max([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
	assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
