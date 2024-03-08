import matplotlib.pyplot as plt


def visualize_expense_income_history(expenses, incomes):
	# Prepare data
	expense_amounts = [expense.amount for expense in expenses]
	income_amounts = [income.amount for income in incomes]

	# Create figure and axis
	fig, ax = plt.subplots()

	# Plot data
	ax.plot(expense_amounts, label='Expenses')
	ax.plot(income_amounts, label='Incomes')

	# Set title and labels
	ax.set_title('Expense and Income History')
	ax.set_xlabel('Time')
	ax.set_ylabel('Amount')

	# Set legend
	ax.legend()

	# Show plot
	plt.show()
