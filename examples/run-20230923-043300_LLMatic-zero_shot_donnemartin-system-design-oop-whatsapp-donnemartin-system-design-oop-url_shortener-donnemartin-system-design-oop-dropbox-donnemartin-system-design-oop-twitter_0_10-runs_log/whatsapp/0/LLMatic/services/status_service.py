import sqlite3
from datetime import datetime

DB_NAME = 'chat.db'

class StatusService:
	@staticmethod
	def post_status(user_id, image, visibility):
		conn = sqlite3.connect(DB_NAME)
		c = conn.cursor()
		c.execute('INSERT INTO statuses (user_id, image, visibility, time_posted) VALUES (?, ?, ?, ?)', (user_id, image, visibility, datetime.now().isoformat()))
		status_id = c.lastrowid
		conn.commit()
		conn.close()
		return {'id': status_id, 'user_id': user_id, 'image': image, 'visibility': visibility, 'time_posted': datetime.now().isoformat()}
