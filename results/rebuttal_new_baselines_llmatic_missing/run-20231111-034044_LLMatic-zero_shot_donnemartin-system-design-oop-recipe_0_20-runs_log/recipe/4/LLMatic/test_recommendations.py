import recommendations


def test_set_and_get_user_preferences():
	recommendations.set_user_preferences('user1', ['Vegan', 'Gluten-free'])
	assert recommendations.get_user_preferences('user1') == ['Vegan', 'Gluten-free']


def test_add_and_get_user_activity():
	recommendations.add_user_activity('user1', 'recipe1')
	assert recommendations.get_user_activity('user1') == ['recipe1']


def test_generate_recommendations():
	recommendations.recipes = {
		'recipe1': {'categories': ['Vegan', 'Gluten-free']},
		'recipe2': {'categories': ['Vegetarian']},
		'recipe3': {'categories': ['Dairy-free']},
		'recipe4': {'categories': ['Vegan', 'Dairy-free']},
		'recipe5': {'categories': ['Gluten-free']}
	}
	recommendations.set_user_preferences('user1', ['Vegan', 'Gluten-free'])
	recommendations.add_user_activity('user1', 'recipe1')
	recs = recommendations.generate_recommendations('user1')
	assert len(recs) <= 5
	assert 'recipe1' not in recs
	assert any(set(recommendations.recipes[recipe]['categories']) & set(['Vegan', 'Gluten-free']) for recipe in recs)
