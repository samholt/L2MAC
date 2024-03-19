def correct_bracketing(brackets: str) -> bool:
	"""Check if every opening bracket has a corresponding closing bracket.

	Args:
		brackets (str): A string of brackets.

	Returns:
		bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
	"""
	counter = 0
	for bracket in brackets:
		if bracket == '(': counter += 1
		elif bracket == ')': counter -= 1
		if counter < 0: return False
	return counter == 0

def test_correct_bracketing():
	assert correct_bracketing('(') == False
	assert correct_bracketing('()') == True
	assert correct_bracketing('(()())') == True
	assert correct_bracketing(')(()') == False
	assert correct_bracketing('(()))') == False
	assert correct_bracketing('((()))') == True
	assert correct_bracketing(')(') == False
