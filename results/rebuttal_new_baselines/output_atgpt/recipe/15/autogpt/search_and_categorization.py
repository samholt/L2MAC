class SearchAndCategorization:
    def __init__(self, recipes):
        self.recipes = recipes

    def search_recipes(self, query):
        # Search for recipes based on ingredients, name, or categories
        results = [recipe for recipe in self.recipes if query in recipe['name'] or query in recipe['ingredients'] or query in recipe['categories']]
        return results

    def categorize_recipes(self, category):
        # Categorize recipes by type, cuisine, or dietary needs
        categorized_recipes = [recipe for recipe in self.recipes if category in recipe['categories']]
        return categorized_recipes