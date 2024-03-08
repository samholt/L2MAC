def analyze_spending_pattern(spending_history):
	total_spending = sum(spending_history)
	average_spending = total_spending / len(spending_history)

	if average_spending > spending_history[-1]:
		return 'Your spending is lower than average. Consider adjusting your budget.'
	else:
		return 'Your spending is higher than average. Consider adjusting your budget.'
