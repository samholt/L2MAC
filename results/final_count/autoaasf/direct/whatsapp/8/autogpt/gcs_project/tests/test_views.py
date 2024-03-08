import unittest
from flask import url_for
from flask_testing import TestCase
import sys
sys.path.append('..')
from app.main import app, db
from app.models import User


class TestViews(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

        self.client.post(url_for('login'), data=dict(username='testuser', password='testpassword'), follow_redirects=True)

        response = self.client.get(url_for('logout'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
