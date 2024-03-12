import pytest
from main import Main
import datetime
import argparse
import sys

def test_integration():
	main = Main()

	# Test account creation
	assert main.create_account('test', 'password') == 'Account created successfully'

	# Test URL shortening
	short_url = main.create_short_url('https://www.google.com')
	assert len(short_url) == 6

	# Test custom URL shortening
	custom_url = main.create_custom_short_url('custom', 'https://www.google.com')
	assert custom_url == 'custom'

	# Test URL expiration
	assert main.set_expiration(short_url, (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')) == 'Expiration date set'

	# Test URL redirection
	assert main.redirect_to_original_url(short_url) == 'https://www.google.com'

	# Test viewing all URLs
	assert len(main.view_all_urls()) == 2

	# Test URL deletion
	main.delete_url(short_url)
	assert main.redirect_to_original_url(short_url) == 'URL not found or expired'

	# Test user deletion
	main.delete_user('test')
	assert main.create_account('test', 'password') == 'Username already exists'

	# Test system monitoring
	assert main.monitor_system() == {'system_performance': 'Good', 'analytics': 'Normal'}

	# Test click tracking
	main.track_click(short_url, 'USA')

	# Test statistics retrieval
	assert len(main.get_statistics(short_url)) > 0

def test_command_line_interface():
	main = Main()
	old_argv = sys.argv

	try:
		sys.argv = ['main.py', '--create_account', 'test', 'password']
		assert 'Account created successfully' in main.main()

		sys.argv = ['main.py', '--create_short_url', 'https://www.google.com']
		short_url = main.main()
		assert len(short_url) == 6

		sys.argv = ['main.py', '--create_custom_short_url', 'custom', 'https://www.google.com']
		assert 'custom' in main.main()

		sys.argv = ['main.py', '--set_expiration', short_url, (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')]
		assert 'Expiration date set' in main.main()

		sys.argv = ['main.py', '--redirect', short_url]
		assert 'https://www.google.com' in main.main()

		sys.argv = ['main.py', '--view_all_urls']
		assert len(main.main()) == 2

		sys.argv = ['main.py', '--delete_url', short_url]
		assert 'URL deleted' in main.main()

		sys.argv = ['main.py', '--delete_user', 'test']
		assert 'User deleted' in main.main()

		sys.argv = ['main.py', '--monitor_system']
		assert 'Good' in main.main()['system_performance'] and 'Normal' in main.main()['analytics']

		sys.argv = ['main.py', '--track_click', short_url, 'USA']
		assert 'Click tracked' in main.main()

		sys.argv = ['main.py', '--get_statistics', short_url]
		assert len(main.main()) > 0

	finally:
		sys.argv = old_argv

