import unittest
from flask import url_for
from app import create_app
from app.database import MockDatabase as db

app, _ = create_app('default')

class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
	self.app.config['WTF_CSRF_SECRET_KEY'] = 'test'
	self.context = self.app.app_context()
	self.context.push()
        self.client = app.test_client()

    def tearDown(self):
	self.context.pop()

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile(self):
        response = self.client.get(url_for('profile'))
        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        response = self.client.get(url_for('edit_profile'))
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        response = self.client.get(url_for('reset_password'))
        self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        response = self.client.get(url_for('send_message'))
        self.assertEqual(response.status_code, 200)

    def test_post_status(self):
        response = self.client.get(url_for('post_status'))
        self.assertEqual(response.status_code, 200)

    def test_group(self):
        response = self.client.get(url_for('group'))
        self.assertEqual(response.status_code, 200)

    def test_block(self):
        response = self.client.get(url_for('block'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

