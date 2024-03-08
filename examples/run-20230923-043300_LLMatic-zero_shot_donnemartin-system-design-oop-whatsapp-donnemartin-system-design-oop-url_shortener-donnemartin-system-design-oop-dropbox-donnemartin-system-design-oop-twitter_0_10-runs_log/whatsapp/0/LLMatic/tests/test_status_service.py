from services.status_service import StatusService
import sqlite3

DB_NAME = 'chat.db'

def test_post_status():
	StatusService.post_status(1, 'image.jpg', 'public')
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute('SELECT * FROM statuses WHERE image = ?', ('image.jpg',))
	status = c.fetchone()
	conn.close()
	assert status is not None
