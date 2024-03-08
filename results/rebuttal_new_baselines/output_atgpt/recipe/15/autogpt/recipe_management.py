class RecipeManagement:
    def __init__(self):
        self.recipes = []

    def submit_recipe(self, recipe):
        # Validate the recipe format
        if self.validate_recipe(recipe):
            self.recipes.append(recipe)
            return True
        return False

    def edit_recipe(self, recipe_id, new_recipe):
        # Validate the new recipe format
        if self.validate_recipe(new_recipe):
            for i, recipe in enumerate(self.recipes):
                if recipe['id'] == recipe_id:
                    self.recipes[i] = new_recipe
                    return True
        return False

    def delete_recipe(self, recipe_id):
        for i, recipe in enumerate(self.recipes):
            if recipe['id'] == recipe_id:
                del self.recipes[i]
                return True
        return False

    def validate_recipe(self, recipe):
        # Check if the recipe has all necessary fields
        required_fields = ['id', 'name', 'ingredients', 'instructions']
        return all(field in recipe for field in required_fields)