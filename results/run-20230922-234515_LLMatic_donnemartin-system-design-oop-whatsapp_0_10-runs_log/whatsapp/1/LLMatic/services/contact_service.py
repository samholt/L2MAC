from sqlalchemy.orm import Session
from models import Contact


def block_contact(db: Session, user_id: int, contact_id: int):
	contact = db.query(Contact).filter(Contact.user_id == user_id, Contact.contact_id == contact_id).first()
	contact.blocked = True
	db.commit()


def unblock_contact(db: Session, user_id: int, contact_id: int):
	contact = db.query(Contact).filter(Contact.user_id == user_id, Contact.contact_id == contact_id).first()
	contact.blocked = False
	db.commit()


def get_contacts(db: Session, user_id: int):
	return db.query(Contact).filter(Contact.user_id == user_id).all()
