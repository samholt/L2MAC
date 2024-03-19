def choose_num(x, y):
	"""This function takes two positive numbers x and y and returns the
	biggest even integer number that is in the range [x, y] inclusive. If 
	there's no such number, then the function should return -1.

	For example:
	choose_num(12, 15) = 14
	choose_num(13, 12) = -1
	"""
	if x > y:
		return -1
	for i in range(y, x-1, -1):
		if i % 2 == 0:
			return i
	return -1

def test_choose_num():
	assert choose_num(12, 15) == 14
	assert choose_num(13, 12) == -1
	assert choose_num(2, 2) == 2
	assert choose_num(1, 1) == -1
	assert choose_num(1, 2) == 2
