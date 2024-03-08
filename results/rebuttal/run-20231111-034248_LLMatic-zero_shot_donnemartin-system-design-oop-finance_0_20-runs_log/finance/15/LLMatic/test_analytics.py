import analytics


def test_generate_monthly_report():
	analytics.DATABASE = {
		'user1': {
			1: {
				'income': [{'amount': 1000}],
				'expenses': [{'amount': 500}]
			},
			2: {
				'income': [{'amount': 2000}],
				'expenses': [{'amount': 1000}]
			}
		}
	}
	report = analytics.generate_monthly_report('user1')
	assert report[1]['income'] == 1000
	assert report[1]['expenses'] == 500
	assert report[2]['income'] == 2000
	assert report[2]['expenses'] == 1000


def test_get_spending_habits():
	analytics.DATABASE = {
		'user1': {
			1: {
				'income': [{'amount': 1000}],
				'expenses': [{'amount': 500}]
			},
			2: {
				'income': [{'amount': 2000}],
				'expenses': [{'amount': 1000}]
			}
		}
	}
	spending_habits = analytics.get_spending_habits('user1')
	assert spending_habits[1]['income'] == 1000
	assert spending_habits[1]['expenses'] == 500
	assert spending_habits[2]['income'] == 2000
	assert spending_habits[2]['expenses'] == 1000


def test_compare_year_on_year():
	analytics.DATABASE = {
		'user1': {
			2019: {
				'income': [{'amount': 1000}],
				'expenses': [{'amount': 500}]
			},
			2020: {
				'income': [{'amount': 2000}],
				'expenses': [{'amount': 1000}]
			}
		}
	}
	comparison = analytics.compare_year_on_year('user1', 2019, 2020)
	assert comparison['year1']['income'] == 1000
	assert comparison['year1']['expenses'] == 500
	assert comparison['year2']['income'] == 2000
	assert comparison['year2']['expenses'] == 1000
