import unittest
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

class TestApp(unittest.TestCase):
	def test_home(self):
		with app.test_client() as c:
			response = c.get('/')
			self.assertEqual(response.data, b'Hello, World!')
