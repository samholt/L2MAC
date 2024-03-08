import pytest
from categories import Category
from database import MockDatabase

def test_add_category():
	db = MockDatabase()
	category = Category(db)
	category.add_category('Vegan', 1)
	assert category.get_recipes_by_category('Vegan') == [1]

def test_remove_recipe_from_category():
	db = MockDatabase()
	category = Category(db)
	category.add_category('Vegan', 1)
	category.remove_recipe_from_category('Vegan', 1)
	assert category.get_recipes_by_category('Vegan') == []
