from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
	""" From a given list of integers, generate a list of rolling maximum element found until given moment
	in the sequence.
	>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
	[1, 2, 3, 3, 3, 4, 4]
	"""
	if not numbers:
		return []
	max_so_far = numbers[0]
	result = [max_so_far]
	for num in numbers[1:]:
		if num > max_so_far:
			max_so_far = num
		result.append(max_so_far)
	return result
