import pytest
import app
from app import User

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return User(id='1', username='test', password='test', bank_accounts=[], expenses={}, incomes={}, budgets={}, investments={})


def test_create_user(client, sample_user):
	response = client.post('/create_user', json=sample_user.__dict__)
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_link_bank_account(client, sample_user):
	app.DATABASE[sample_user.id] = sample_user
	response = client.post('/link_bank_account', json={'user_id': sample_user.id, 'bank_account': '1234567890'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Bank account linked successfully'}


def test_add_expense(client, sample_user):
	app.DATABASE[sample_user.id] = sample_user
	response = client.post('/add_expense', json={'user_id': sample_user.id, 'expense': {'category': 'Food', 'amount': 100}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Expense added successfully'}


def test_add_income(client, sample_user):
	app.DATABASE[sample_user.id] = sample_user
	response = client.post('/add_income', json={'user_id': sample_user.id, 'income': {'source': 'Salary', 'amount': 1000}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Income added successfully'}


def test_set_budget(client, sample_user):
	app.DATABASE[sample_user.id] = sample_user
	response = client.post('/set_budget', json={'user_id': sample_user.id, 'budget': {'category': 'Food', 'amount': 500}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Budget set successfully'}


def test_add_investment(client, sample_user):
	app.DATABASE[sample_user.id] = sample_user
	response = client.post('/add_investment', json={'user_id': sample_user.id, 'investment': {'type': 'Stock', 'amount': 1000}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Investment added successfully'}
