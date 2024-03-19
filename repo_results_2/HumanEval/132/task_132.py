def is_nested(string):
	'''Create a function that takes a string as input which contains only square brackets.
	The function should return True if and only if there is a valid subsequence of brackets 
	where at least one bracket in the subsequence is nested.
	'''
	depth = 0
	for char in string:
		if char == '[':
			depth += 1
		elif char == ']':
			depth -= 1
		if depth < 0:
			return False
		if depth >= 2:
			return True
	return False

def test_is_nested():
	assert is_nested('[[]]') == True
	assert is_nested('[]]]]]]][[[[[]') == False
	assert is_nested('[][]') == False
	assert is_nested('[]') == False
	assert is_nested('[[][]]') == True
	assert is_nested('[[]][[') == True
	assert is_nested('') == False
	assert is_nested('[') == False
	assert is_nested(']') == False
	assert is_nested('][') == False
	assert is_nested('[[[[]]]]') == True
