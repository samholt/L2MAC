from reminder import Reminder

def test_create_reminder():
	reminder = Reminder()
	assert reminder.create_reminder(1, '2022-12-31 11:00:00', 'This is a reminder for the test meeting') == 1

def test_get_reminder():
	reminder = Reminder()
	assert reminder.get_reminder(1) == 'Reminder not found'

def test_update_reminder():
	reminder = Reminder()
	assert reminder.update_reminder(1, 1, '2022-12-31 11:30:00', 'This is an updated reminder for the test meeting') == 'Reminder not found'

def test_delete_reminder():
	reminder = Reminder()
	assert reminder.delete_reminder(1) == 'Reminder not found'
