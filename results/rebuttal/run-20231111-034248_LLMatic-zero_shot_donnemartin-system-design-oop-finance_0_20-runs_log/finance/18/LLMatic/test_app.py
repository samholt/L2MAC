import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_authenticate(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/authenticate', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Authentication successful'}


def test_recover_password(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/recover_password', json={'username': 'test'})
	assert response.status_code == 200
	assert 'password' in response.get_json()


def test_set_budget(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/set_budget', json={'username': 'test', 'password': 'test', 'category': 'food', 'amount': 100})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Budget set successfully'}


def test_check_budget(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	client.post('/set_budget', json={'username': 'test', 'password': 'test', 'category': 'food', 'amount': 100})
	response = client.post('/check_budget', json={'username': 'test', 'password': 'test', 'category': 'food'})
	assert response.status_code == 200
	assert 'over_budget' in response.get_json()


def test_track_progress(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	client.post('/set_budget', json={'username': 'test', 'password': 'test', 'category': 'food', 'amount': 100})
	response = client.post('/track_progress', json={'username': 'test', 'password': 'test', 'category': 'food'})
	assert response.status_code == 200
	assert 'progress' in response.get_json()


def test_generate_monthly_report(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/generate_monthly_report', json={'username': 'test', 'password': 'test', 'month': 1, 'year': 2022})
	assert response.status_code == 200
	assert 'report' in response.get_json()


def test_visualize_spending_habits(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/visualize_spending_habits', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'spending' in response.get_json()


def test_compare_year_on_year(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/compare_year_on_year', json={'username': 'test', 'password': 'test', 'year1': 2021, 'year2': 2022})
	assert response.status_code == 200
	assert 'comparison' in response.get_json()


def test_get_savings_tips(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/get_savings_tips', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'tips' in response.get_json()


def test_get_product_recommendations(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/get_product_recommendations', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'recommendations' in response.get_json()


def test_get_notifications(client):
	client.post('/create_user', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	response = client.post('/get_notifications', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'notifications' in response.get_json()

