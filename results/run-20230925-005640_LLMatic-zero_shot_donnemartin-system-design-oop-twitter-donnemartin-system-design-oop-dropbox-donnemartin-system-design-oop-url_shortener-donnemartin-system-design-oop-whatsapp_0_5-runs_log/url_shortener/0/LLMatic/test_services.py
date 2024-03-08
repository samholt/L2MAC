from services import generate_short_url, get_original_url
from models import User
from datetime import datetime, timedelta
import time

# existing tests...

def test_url_expiration():
	user = User('test', 'test')
	short_url = generate_short_url('http://test.com', user, None, datetime.now() + timedelta(seconds=1))
	assert get_original_url(short_url) is not None
	time.sleep(2)
	assert get_original_url(short_url) is None

