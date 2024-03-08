import reviews


def test_submit_review():
	review = reviews.submit_review('test_user', 'test_recipe', 5, 'Great recipe!')
	assert review.username == 'test_user'
	assert review.recipe == 'test_recipe'
	assert review.rating == 5
	assert review.review_text == 'Great recipe!'


def test_get_review():
	review = reviews.get_review('test_user')
	assert review.username == 'test_user'
	assert review.recipe == 'test_recipe'
	assert review.rating == 5
	assert review.review_text == 'Great recipe!'

