def count_nums(arr):
	"""
	Write a function count_nums which takes an array of integers and returns
	the number of elements which has a sum of digits > 0.
	If a number is negative, then its first signed digit will be negative:
	e.g. -123 has signed digits -1, 2, and 3.
	>>> count_nums([]) == 0
	>>> count_nums([-1, 11, -11]) == 1
	>>> count_nums([1, 1, 2]) == 3
	"""
	count = 0
	for num in arr:
		str_num = str(num)
		if num < 0:
			str_num = str_num[1:]
			sum_digits = -int(str_num[0])
			str_num = str_num[1:]
		else:
			sum_digits = 0
		for digit in str_num:
			sum_digits += int(digit)
		if sum_digits > 0:
			count += 1
	return count
