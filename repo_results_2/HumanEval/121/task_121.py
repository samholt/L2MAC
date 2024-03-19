def solution(lst):
	"""Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

	Examples
	solution([5, 8, 7, 1]) ==> 12
	solution([3, 3, 3, 3, 3]) ==> 9
	solution([30, 13, 24, 321]) ==>0
	"""
	return sum([num for idx, num in enumerate(lst) if idx % 2 == 0 and num % 2 != 0])

def test_solution():
	assert solution([5, 8, 7, 1]) == 12
	assert solution([3, 3, 3, 3, 3]) == 9
	assert solution([30, 13, 24, 321]) == 0
	assert solution([1, 2, 3, 4, 5]) == 4
	assert solution([2, 4, 6, 8, 10]) == 0
