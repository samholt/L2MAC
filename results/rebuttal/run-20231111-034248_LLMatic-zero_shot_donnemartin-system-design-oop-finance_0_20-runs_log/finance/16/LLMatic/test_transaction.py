import transaction


def test_enter_transaction():
	trans = transaction.Transaction('test_user', 100, 'groceries', 'expense')
	assert trans.enter_transaction() == 'Transaction entered'


def test_upload_transaction():
	trans = transaction.Transaction('test_user', 100, 'groceries', 'expense')
	assert trans.upload_transaction() == 'Transaction data uploaded'


def test_categorize_transaction():
	trans = transaction.Transaction('test_user', 100, 'groceries', 'expense')
	assert trans.categorize_transaction() == 'Transaction categorized'


def test_classify_recurring():
	trans = transaction.Transaction('test_user', 100, 'groceries', 'expense')
	trans.classify_recurring()
	assert trans.recurring == True
