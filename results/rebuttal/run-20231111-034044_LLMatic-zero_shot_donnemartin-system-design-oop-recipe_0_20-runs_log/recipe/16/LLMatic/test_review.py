from review import Review

def test_review_creation():
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	assert review.user == 'user1'
	assert review.recipe == 'recipe1'
	assert review.rating == 5
	assert review.text == 'Great recipe!'


def test_write_review():
	db = {}
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	review.write_review(db)
	assert len(db) == 1
	assert db[1] == review


def test_delete_review():
	db = {}
	review = Review('user1', 'recipe1', 5, 'Great recipe!')
	review.write_review(db)
	review.delete_review(db)
	assert len(db) == 0
