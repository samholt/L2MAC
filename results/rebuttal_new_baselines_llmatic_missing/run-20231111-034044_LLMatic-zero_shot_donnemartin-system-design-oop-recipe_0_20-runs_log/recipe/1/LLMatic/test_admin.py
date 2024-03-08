from admin import Admin
from recipe import Recipe
from review import Review

def test_manage_recipes():
	admin = Admin('admin', 'admin')
	recipe = Recipe(['ingredient1', 'ingredient2'], 'instructions', 'images', 'category', 'dietary_needs', 'timestamp')
	recipe.submit_recipe()
	assert admin.manage_recipes(recipe) == 'Recipe removed successfully'


def test_remove_inappropriate_content():
	admin = Admin('admin', 'admin')
	review = Review('user', 'recipe', 3, 'content')
	review.submit_review()
	assert admin.remove_inappropriate_content(review) == 'Review removed successfully'
