from reviews import Review

def test_reviews():
	review = Review()
	review.add_review('user1', 'recipe1', 5, 'Great!')
	review.add_review('user2', 'recipe1', 4, 'Good')
	assert review.get_average_rating('recipe1') == 4.5
	review.edit_review('user1', 'recipe1', 3, 'Average')
	assert review.get_average_rating('recipe1') == 3.5
