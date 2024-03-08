import sqlite3
from models.contact import Contact

def create_contacts_table():
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS contacts (user_id INTEGER, contact_id INTEGER, blocked INTEGER)')

def block_contact(user_id: int, contact_id: int) -> Contact:
	create_contacts_table()
	contact = Contact(user_id=user_id, contact_id=contact_id, blocked=True)
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('INSERT INTO contacts (user_id, contact_id, blocked) VALUES (?, ?, ?)', (contact.user_id, contact.contact_id, int(contact.blocked)))
	return contact

def unblock_contact(user_id: int, contact_id: int) -> Contact:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('UPDATE contacts SET blocked = 0 WHERE user_id = ? AND contact_id = ?', (user_id, contact_id))
		return get_contact(user_id, contact_id)

def get_contact(user_id: int, contact_id: int) -> Contact:
	with sqlite3.connect('gcs.db') as conn:
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM contacts WHERE user_id = ? AND contact_id = ?', (user_id, contact_id))
		contact_data = cursor.fetchone()
		if contact_data is None:
			return None
		return Contact(user_id=contact_data[0], contact_id=contact_data[1], blocked=bool(contact_data[2]))
