def check_dict_case(dict):
	"""
	Given a dictionary, return True if all keys are strings in lower 
	case or all keys are strings in upper case, else return False.
	The function should return False is the given dictionary is empty.
	Examples:
	check_dict_case({"a":"apple", "b":"banana"}) should return True.
	check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
	check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
	check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
	check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
	"""
	if not dict:
		return False
	is_lower = is_upper = None
	for key in dict:
		if not isinstance(key, str):
			return False
		if is_lower is None and is_upper is None:
			is_lower = key.islower()
			is_upper = key.isupper()
		elif is_lower and not key.islower() or is_upper and not key.isupper():
			return False
	return is_lower or is_upper
