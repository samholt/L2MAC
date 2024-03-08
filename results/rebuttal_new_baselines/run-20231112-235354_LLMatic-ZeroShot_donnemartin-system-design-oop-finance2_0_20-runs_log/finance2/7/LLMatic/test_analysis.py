import pytest
from analysis import analyze_spending_pattern

def test_analysis():
	assert analyze_spending_pattern([100, 200, 300, 400, 500]) == 'Your spending is higher than average. Consider adjusting your budget.'
	assert analyze_spending_pattern([500, 400, 300, 200, 100]) == 'Your spending is lower than average. Consider adjusting your budget.'
