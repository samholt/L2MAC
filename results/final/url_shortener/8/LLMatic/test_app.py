from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views)


def test_app():
	with app.test_client() as client:
		response = client.get('/')
		assert response.status_code == 404
