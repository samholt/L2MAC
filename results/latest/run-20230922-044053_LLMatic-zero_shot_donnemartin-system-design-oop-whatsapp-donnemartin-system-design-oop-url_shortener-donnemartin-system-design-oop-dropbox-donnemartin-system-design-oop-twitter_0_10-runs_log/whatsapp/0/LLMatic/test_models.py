import unittest
from app import app, db
from models import User, Contact

class UserModelCase(unittest.TestCase):
	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_contact_management(self):
		# create a new user
		u = User(email='john@example.com')
		u.set_password('cat')
		db.session.add(u)
		db.session.commit()

		# add a contact to the user
		c = Contact(user_id=u.id, contact_id=2)
		u.contacts.append(c)
		db.session.commit()

		# check if the contact is added
		self.assertEqual(u.contacts.count(), 1)
		self.assertEqual(u.contacts.first().contact_id, 2)

		# block the contact
		u.block_contact(c)
		self.assertEqual(u.contacts.first().blocked, True)

		# unblock the contact
		u.unblock_contact(c)
		self.assertEqual(u.contacts.first().blocked, False)

if __name__ == '__main__':
	unittest.main(verbosity=2)
