import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from app import create_app, db
from app.models import User, ActivityLog


class CloudSafeTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Write test cases here


if __name__ == '__main__':
    unittest.main()
