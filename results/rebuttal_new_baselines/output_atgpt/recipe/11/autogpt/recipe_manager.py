class RecipeManager:
    def __init__(self):
        self.recipes = []

    def submit_recipe(self, recipe):
        # Validate recipe format
        if not self.validate_recipe_format(recipe):
            return 'Invalid recipe format'
        # Add recipe to list
        self.recipes.append(recipe)
        return 'Recipe submitted successfully'

    def edit_recipe(self, recipe_id, updated_recipe):
        # Find recipe by id
        for i, recipe in enumerate(self.recipes):
            if recipe['id'] == recipe_id:
                # Update recipe
                self.recipes[i] = updated_recipe
                return 'Recipe updated successfully'
        return 'Recipe not found'

    def delete_recipe(self, recipe_id):
        # Find and delete recipe by id
        for i, recipe in enumerate(self.recipes):
            if recipe['id'] == recipe_id:
                del self.recipes[i]
                return 'Recipe deleted successfully'
        return 'Recipe not found'

    def validate_recipe_format(self, recipe):
        # Check if recipe has all necessary fields
        required_fields = ['id', 'name', 'ingredients', 'instructions']
        return all(field in recipe for field in required_fields)