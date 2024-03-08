import sqlite3

DB_NAME = 'chat.db'

class UserService:
	@staticmethod
	def create_group(name, picture, participants, admins):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('INSERT INTO groups (name, picture, participants, admins) VALUES (?, ?, ?, ?)', (name, picture, str(participants), str(admins)))
		group_id = c.lastrowid
		conn.commit()
		conn.close()
		return {'id': group_id, 'name': name, 'picture': picture, 'participants': participants, 'admins': admins}

	@staticmethod
	def edit_group(group_id, name=None, picture=None, participants=None, admins=None):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('UPDATE groups SET name = ?, picture = ?, participants = ?, admins = ? WHERE id = ?', (name, picture, str(participants), str(admins), group_id))
		conn.commit()
		conn.close()
		return {'id': group_id, 'name': name, 'picture': picture, 'participants': participants, 'admins': admins}

	@staticmethod
	def get_online_status(user_id):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('SELECT online FROM users WHERE id = ?', (user_id,))
		online_status = c.fetchone()
		conn.close()
		return online_status[0] if online_status else None
