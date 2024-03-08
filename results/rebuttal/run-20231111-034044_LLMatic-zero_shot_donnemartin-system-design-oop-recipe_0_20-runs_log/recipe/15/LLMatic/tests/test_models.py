import models

def test_user_model():
	user = models.User('username', 'password', 'email', [])
	assert user.username == 'username'
	assert user.password == 'password'
	assert user.email == 'email'
	assert user.favorite_recipes == []
	assert user.submitted_recipes == []

def test_recipe_model():
	recipe = models.Recipe('name', 'ingredients', 'instructions', 'image', ['categories'], 'submitted_by')
	assert recipe.name == 'name'
	assert recipe.ingredients == 'ingredients'
	assert recipe.instructions == 'instructions'
	assert recipe.image == 'image'
	assert recipe.categories == ['categories']
	assert recipe.submitted_by == 'submitted_by'

def test_review_model():
	review = models.Review('username', 'recipe_name', 5, 'comment')
	assert review.username == 'username'
	assert review.recipe_name == 'recipe_name'
	assert review.rating == 5
	assert review.comment == 'comment'

def test_follow_model():
	follow = models.Follow('follower', 'following')
	assert follow.follower == 'follower'
	assert follow.following == 'following'

