def closest_integer(value):
	'''Create a function that takes a value (string) representing a number
	and returns the closest integer to it. If the number is equidistant
	from two integers, round it away from zero.

	Examples
	>>> closest_integer("10")
	10
	>>> closest_integer("15.3")
	15

	Note:
	Rounding away from zero means that if the given number is equidistant
	from two integers, the one you should return is the one that is the
	farthest from zero. For example closest_integer("14.5") should
	return 15 and closest_integer("-14.5") should return -15.
	'''
	# Convert the string to a float
	num = float(value)
	# If the number is positive, round up if the decimal part is >= 0.5
	# If the number is negative, round down if the decimal part is > 0.5
	if num >= 0:
		return int(num) if num - int(num) < 0.5 else int(num) + 1
	else:
		return int(num) if int(num) - num < 0.5 else int(num) - 1

def test_closest_integer():
	assert closest_integer('10') == 10
	assert closest_integer('15.3') == 15
	assert closest_integer('14.5') == 15
	assert closest_integer('-14.5') == -15
	assert closest_integer('0') == 0
	assert closest_integer('-0.5') == -1
	assert closest_integer('0.5') == 1
