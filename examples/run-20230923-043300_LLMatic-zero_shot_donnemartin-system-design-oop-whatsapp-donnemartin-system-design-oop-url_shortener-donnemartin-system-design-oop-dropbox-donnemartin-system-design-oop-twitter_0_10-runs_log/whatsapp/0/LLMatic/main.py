import sqlite3

def setup_db():
	conn = sqlite3.connect('user_db.sqlite')
	c = conn.cursor()
	c.execute('''
		CREATE TABLE IF NOT EXISTS User (
			id INTEGER PRIMARY KEY,
			email TEXT,
			password TEXT,
			profile_picture TEXT,
			status_message TEXT,
			privacy_settings TEXT,
			blocked_contacts TEXT
		)
	''')
	c.execute('''
		CREATE TABLE IF NOT EXISTS Group (
			id INTEGER PRIMARY KEY,
			name TEXT,
			picture TEXT,
			admin_id INTEGER
		)
	''')
	c.execute('''
		CREATE TABLE IF NOT EXISTS GroupMember (
			group_id INTEGER,
			user_id INTEGER
		)
	''')
	conn.commit()
	conn.close()

if __name__ == '__main__':
	setup_db()
