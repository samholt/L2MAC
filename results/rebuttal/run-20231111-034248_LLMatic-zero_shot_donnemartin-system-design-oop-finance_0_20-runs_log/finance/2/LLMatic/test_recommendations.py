import recommendations


def test_recommendations():
	rec = recommendations.Recommendations()
	rec.add_recommendation('user1', {'product': 'High-interest savings account'})
	assert rec.get_recommendations('user1') == [{'product': 'High-interest savings account'}]
	rec.clear_recommendations('user1')
	assert rec.get_recommendations('user1') == []


def test_savings_tips():
	rec = recommendations.Recommendations()
	spending_habits = {'food': 400, 'entertainment': 200, 'transportation': 200}
	budget = 1000
	rec.generate_savings_tips('user1', spending_habits, budget)
	tips = rec.get_recommendations('user1')[0]['savings_tips']
	assert 'Consider cooking at home to save on food expenses.' in tips
	assert 'Consider reducing entertainment expenses.' in tips
	assert 'Consider using public transportation to save on transportation costs.' in tips
