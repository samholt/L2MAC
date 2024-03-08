import sqlite3

DB_NAME = 'chat.db'

class GroupService:
	@staticmethod
	def create_group(name, participants):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('INSERT INTO groups (name, participants) VALUES (?, ?)', (name, str(participants)))
		group_id = c.lastrowid
		conn.commit()
		conn.close()
		return {'id': group_id, 'name': name, 'participants': participants}
