def correct_bracketing(brackets: str) -> bool:
	""" brackets is a string of "<" and ">".
	return True if every opening bracket has a corresponding closing bracket.
	"""
	stack = []
	for bracket in brackets:
		if bracket == '<':
			stack.append(bracket)
		elif bracket == '>':
			if not stack:
				return False
			stack.pop()
	return not stack

def test_correct_bracketing():
	assert not correct_bracketing('<')
	assert correct_bracketing('<>')
	assert correct_bracketing('<<><>>')
	assert not correct_bracketing('><<>')
	assert correct_bracketing('')
	assert not correct_bracketing('>')
	assert not correct_bracketing('><')
	assert not correct_bracketing('><>')
