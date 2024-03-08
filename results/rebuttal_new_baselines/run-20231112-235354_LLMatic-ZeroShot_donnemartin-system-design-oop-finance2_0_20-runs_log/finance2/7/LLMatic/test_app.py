import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'otp' in response.get_json()


def test_add_expense(client):
	response = client.post('/expense', json={'username': 'test', 'id': 1, 'amount': 100, 'date': '2022-01-01'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Expense added successfully'


def test_add_income(client):
	response = client.post('/income', json={'username': 'test', 'id': 1, 'amount': 1000, 'source': 'Salary', 'date': '2022-01-01'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Income added successfully'


def test_set_budget(client):
	response = client.post('/budget', json={'username': 'test', 'monthly_budget': 5000})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Budget set successfully'


def test_integrate_investment(client):
	response = client.post('/investment', json={'username': 'test', 'investment_info': {'broker': 'Broker1', 'account_number': '123456'}})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Investment integrated successfully'


def test_get_report(client):
	response = client.get('/report', query_string={'username': 'test', 'type': 'monthly_summary'})
	assert response.status_code == 200
	assert 'report' in response.get_json()
