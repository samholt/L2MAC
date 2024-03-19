def compare_one(a, b):
	"""
	Create a function that takes integers, floats, or strings representing
	real numbers, and returns the larger variable in its given variable type.
	Return None if the values are equal.
	Note: If a real number is represented as a string, the floating point might be . or ,
	"""
	def convert_to_float(val):
		if isinstance(val, str):
			val = val.replace(',', '.')
			return float(val)
		return val

	a_float = convert_to_float(a)
	b_float = convert_to_float(b)

	if a_float > b_float:
		return a
	elif a_float < b_float:
		return b
	else:
		return None
