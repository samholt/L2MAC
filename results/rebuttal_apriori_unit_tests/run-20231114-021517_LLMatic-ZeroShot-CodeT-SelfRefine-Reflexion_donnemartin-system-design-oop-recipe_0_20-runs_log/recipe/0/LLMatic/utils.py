def validate_recipe(data):
	required_fields = ['title', 'ingredients', 'instructions', 'image']
	if not all(field in data and data[field] for field in required_fields):
		return False
	return True
