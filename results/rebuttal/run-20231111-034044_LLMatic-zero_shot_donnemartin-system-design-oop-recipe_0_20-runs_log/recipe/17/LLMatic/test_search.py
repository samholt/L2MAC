import pytest
from search import Search
from recipe import Recipe


def test_search_by_ingredient():
	recipe1 = Recipe('Pancakes', ['flour', 'milk', 'eggs'], '', '', [])
	recipe2 = Recipe('Omelette', ['eggs', 'milk'], '', '', [])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.search_by_ingredient('eggs')
	assert len(results) == 2
	assert recipe1 in results
	assert recipe2 in results


def test_search_by_name():
	recipe1 = Recipe('Pancakes', [], '', '', [])
	recipe2 = Recipe('Omelette', [], '', '', [])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.search_by_name('pancakes')
	assert len(results) == 1
	assert recipe1 in results


def test_search_by_category():
	recipe1 = Recipe('Pancakes', [], '', '', ['breakfast'])
	recipe2 = Recipe('Omelette', [], '', '', ['breakfast'])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.search_by_category('breakfast')
	assert len(results) == 2
	assert recipe1 in results
	assert recipe2 in results


def test_categorize_by_type():
	recipe1 = Recipe('Pancakes', [], '', '', ['breakfast'])
	recipe2 = Recipe('Omelette', [], '', '', ['breakfast'])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.categorize_by_type('breakfast')
	assert len(results) == 2
	assert recipe1 in results
	assert recipe2 in results


def test_categorize_by_cuisine():
	recipe1 = Recipe('Pancakes', [], '', '', ['american'])
	recipe2 = Recipe('Omelette', [], '', '', ['french'])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.categorize_by_cuisine('american')
	assert len(results) == 1
	assert recipe1 in results


def test_categorize_by_diet():
	recipe1 = Recipe('Pancakes', [], '', '', ['vegetarian'])
	recipe2 = Recipe('Omelette', [], '', '', ['vegetarian'])
	database = {'1': recipe1, '2': recipe2}
	search = Search(database)
	results = search.categorize_by_diet('vegetarian')
	assert len(results) == 2
	assert recipe1 in results
	assert recipe2 in results
