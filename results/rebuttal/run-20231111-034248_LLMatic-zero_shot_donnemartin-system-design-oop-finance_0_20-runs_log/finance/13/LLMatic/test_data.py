import datetime
from data import Data, Transaction

def test_send_notification():
	data = Data()
	message = 'Test notification'
	assert data.send_notification(message) == 'Notification: ' + message

def test_alert_unusual_activity():
	data = Data()
	transaction1 = Transaction(1, 'expense', 50, 'groceries', datetime.datetime.now())
	transaction2 = Transaction(2, 'expense', 200, 'groceries', datetime.datetime.now())
	data.add_transaction(transaction1)
	assert data.alert_unusual_activity(transaction2) == 'Notification: Unusual activity detected in groceries transactions.'
	assert data.alert_unusual_activity(transaction1) == 'No unusual activity detected.'
