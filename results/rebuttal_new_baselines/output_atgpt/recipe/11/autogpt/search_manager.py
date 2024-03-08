class SearchManager:
    def __init__(self, recipe_manager):
        self.recipe_manager = recipe_manager

    def search_by_ingredient(self, ingredient):
        # Find recipes that contain the ingredient
        return [recipe for recipe in self.recipe_manager.recipes if ingredient in recipe['ingredients']]

    def search_by_name(self, name):
        # Find recipes that match the name
        return [recipe for recipe in self.recipe_manager.recipes if name in recipe['name']]

    def search_by_category(self, category):
        # Find recipes that match the category
        return [recipe for recipe in self.recipe_manager.recipes if category in recipe['categories']]

    def categorize_by_type(self, type):
        # Categorize recipes by type
        return [recipe for recipe in self.recipe_manager.recipes if type == recipe['type']]

    def categorize_by_cuisine(self, cuisine):
        # Categorize recipes by cuisine
        return [recipe for recipe in self.recipe_manager.recipes if cuisine == recipe['cuisine']]

    def categorize_by_diet(self, diet):
        # Categorize recipes by dietary needs
        return [recipe for recipe in self.recipe_manager.recipes if diet in recipe['diet']]