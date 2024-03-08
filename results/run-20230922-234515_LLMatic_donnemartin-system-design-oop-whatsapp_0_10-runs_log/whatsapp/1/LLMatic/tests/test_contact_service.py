from services import contact_service
from models import Contact


def test_block_contact(db):
	user_id = 1
	contact_id = 2
	contact_service.block_contact(db, user_id, contact_id)
	contact = db.query(Contact).filter(Contact.user_id == user_id, Contact.contact_id == contact_id).first()
	assert contact.blocked == True


def test_unblock_contact(db):
	user_id = 1
	contact_id = 2
	contact_service.unblock_contact(db, user_id, contact_id)
	contact = db.query(Contact).filter(Contact.user_id == user_id, Contact.contact_id == contact_id).first()
	assert contact.blocked == False


def test_get_contacts(db):
	user_id = 1
	contacts = contact_service.get_contacts(db, user_id)
	assert isinstance(contacts, list)
