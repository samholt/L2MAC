import app
from models.user import User
from models.investment import Investment

def test_track_investment_performance():
	user = User('test', 'test@test.com', 'password')
	investment = Investment(user, 1000, 'Stocks')
	with app.app.test_client() as c:
		response = c.post('/track_investment_performance', json={'user': 'test'})
		assert response.status_code == 200
		assert response.get_json()['investment']['user']['name'] == 'test'
		assert response.get_json()['investment']['amount'] == 1000
		assert response.get_json()['investment']['type'] == 'Stocks'
		assert response.get_json()['performance'] == 'Good'
