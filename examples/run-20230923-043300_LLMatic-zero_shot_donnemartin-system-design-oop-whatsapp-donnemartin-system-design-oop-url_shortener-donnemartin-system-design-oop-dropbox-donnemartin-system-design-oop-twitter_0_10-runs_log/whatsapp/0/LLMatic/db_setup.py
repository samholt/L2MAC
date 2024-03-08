import sqlite3

DB_NAME = 'chat.db'

def setup_database():
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	# Create users table
	c.execute('''
		CREATE TABLE users (
			id INTEGER PRIMARY KEY,
			email TEXT NOT NULL,
			password TEXT NOT NULL,
			profile_picture TEXT,
			status_message TEXT,
			privacy_settings TEXT NOT NULL
		)
	''')

	# Create contacts table
	c.execute('''
		CREATE TABLE contacts (
			id INTEGER PRIMARY KEY,
			user_id INTEGER NOT NULL,
			contact_id INTEGER NOT NULL,
			blocked INTEGER NOT NULL
		)
	''')

	# Create groups table
	c.execute('''
		CREATE TABLE groups (
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL,
			picture TEXT,
			participants TEXT NOT NULL,
			admin_roles TEXT NOT NULL
		)
	''')

	# Create messages table
	c.execute('''
		CREATE TABLE messages (
			id INTEGER PRIMARY KEY,
			sender INTEGER NOT NULL,
			receiver INTEGER NOT NULL,
			message TEXT NOT NULL,
			read_receipt INTEGER NOT NULL,
			encrypted INTEGER NOT NULL
		)
	''')

	# Create statuses table
	c.execute('''
		CREATE TABLE statuses (
			id INTEGER PRIMARY KEY,
			user_id INTEGER NOT NULL,
			image TEXT NOT NULL,
			visibility TEXT NOT NULL,
			time_posted TEXT NOT NULL
		)
	''')

	conn.commit()
	conn.close()

if __name__ == '__main__':
	setup_database()
