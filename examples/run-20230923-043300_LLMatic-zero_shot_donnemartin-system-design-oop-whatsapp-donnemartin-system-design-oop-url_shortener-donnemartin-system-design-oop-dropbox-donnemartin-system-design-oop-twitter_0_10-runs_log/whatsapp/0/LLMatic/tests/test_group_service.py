from services.group_service import GroupService
import sqlite3

DB_NAME = 'chat.db'

def test_create_group():
	GroupService.create_group('Test Group', ['test@test.com'])
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute('SELECT * FROM groups WHERE name = ?', ('Test Group',))
	group = c.fetchone()
	conn.close()
	assert group is not None
