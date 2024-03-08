from models import Recipe


def search_recipes(query, search_type):
	if search_type == 'ingredient':
		return [recipe for recipe in Recipe.all() if query in recipe.ingredients]
	elif search_type == 'name':
		return [recipe for recipe in Recipe.all() if query in recipe.title]
	elif search_type == 'category':
		return [recipe for recipe in Recipe.all() if query in recipe.categories]


def categorize_recipes(category, categorization_type):
	if categorization_type == 'type':
		return [recipe for recipe in Recipe.all() if recipe.type and category in recipe.type]
	elif categorization_type == 'cuisine':
		return [recipe for recipe in Recipe.all() if recipe.cuisine and category in recipe.cuisine]
	elif categorization_type == 'dietary_needs':
		return [recipe for recipe in Recipe.all() if recipe.dietary_needs and category in recipe.dietary_needs]
