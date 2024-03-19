def change_base(x: int, base: int) -> str:
	"""Change numerical base of input number x to base.
	return string representation after the conversion.
	base numbers are less than 10.
	>>> change_base(8, 3)
	'22'
	>>> change_base(8, 2)
	'1000'
	>>> change_base(7, 2)
	'111'
	"""
	result = ''
	while x > 0:
		x, remainder = divmod(x, base)
		result = str(remainder) + result
	return result


# For base greater than 10

ALPHABET = '0123456789abcdef'


def change_base_v2(x: int, base: int) -> str:
	"""Change numerical base of input number x to base.
	return string representation after the conversion.
	base numbers are less than 16.
	>>> change_base_v2(255, 16)
	'ff'
	"""
	result = ''
	while x > 0:
		x, remainder = divmod(x, base)
		result = ALPHABET[remainder] + result
	return result
