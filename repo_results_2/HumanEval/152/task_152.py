def compare(game, guess):
	"""Determine if a person correctly guessed the results of a number of matches.
	Given two arrays of scores and guesses of equal length, where each index shows a match.
	Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
	the value is 0, and if not, the value is the absolute difference between the guess and the score.
	
	:param game: list of integers representing the scores of a number of matches
	:param guess: list of integers representing the guesses for those scores
	:return: list of integers representing how far off each guess was
	"""
	return [abs(g - s) for g, s in zip(game, guess)]


def test_compare():
	assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]
	assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]
	assert compare([0,0,0,0,0,0],[0,0,0,0,0,0]) == [0,0,0,0,0,0]
	assert compare([1,1,1,1,1,1],[0,0,0,0,0,0]) == [1,1,1,1,1,1]
	assert compare([1,2,3,4,5,6],[-1,-2,-3,-4,-5,-6]) == [2,4,6,8,10,12]
