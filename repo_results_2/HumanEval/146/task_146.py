def specialFilter(nums):
	"""Write a function that takes an array of numbers as input and returns
	the number of elements in the array that are greater than 10 and both
	first and last digits of a number are odd (1, 3, 5, 7, 9).
	For example:
	specialFilter([15, -73, 14, -15]) => 1
	specialFilter([33, -2, -3, 45, 21, 109]) => 2
	"""
	count = 0
	for num in nums:
		if num > 10:
			str_num = str(num)
			if int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0:
				count += 1
	return count

def test_specialFilter():
	assert specialFilter([15, -73, 14, -15]) == 1
	assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
	assert specialFilter([11, 13, 15, 17, 19]) == 5
	assert specialFilter([10, 20, 30, 40, 50]) == 0
	assert specialFilter([]) == 0
