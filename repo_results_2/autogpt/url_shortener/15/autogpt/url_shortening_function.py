import urllib.request
import uuid
import webbrowser
import datetime
import geocoder

users = {}
url_expirations = {}

def shorten_url(url, custom_short_url=None, username=None, expiration=None):
    # Validate URL
    if not validate_url(url):
        return 'Invalid URL'
    # Generate unique shortened URL or use custom short URL if provided and not in use
    short_url = custom_short_url if custom_short_url and not is_in_use(custom_short_url) else generate_short_url()
    # Store both URLs in file
    store_in_file(url, short_url)
    # Associate shortened URL with user
    if username:
        if username not in users:
            users[username] = []
        users[username].append(short_url)
    # Set expiration date/time
    if expiration:
        url_expirations[short_url] = expiration
    return short_url

def validate_url(url):
    # Implement URL validation logic
    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False

def generate_short_url():
    # Implement logic for generating unique shortened URLs
    return str(uuid.uuid4())[:8]

def store_in_file(url, short_url):
    # Implement logic for storing URLs in file
    with open('url_database.txt', 'a') as f:
        f.write(f'{short_url} {url}\n')

def is_in_use(short_url):
    # Implement logic for checking if a short URL is already in use
    with open('url_database.txt', 'r') as f:
        for line in f:
            if line.split()[0] == short_url:
                return True
    return False

def redirect(short_url):
    # Implement redirection functionality
    if short_url in url_expirations and datetime.datetime.now() > url_expirations[short_url]:
        print('URL has expired')
        return
    with open('url_database.txt', 'r') as f:
        for line in f:
            if line.split()[0] == short_url:
                webbrowser.open(line.split()[1])
                track_click(short_url)
                return
    print('Short URL not found')

def track_click(short_url):
    # Implement analytics features
    with open('analytics.txt', 'a') as f:
        f.write(f'{short_url} {datetime.datetime.now()} {geocoder.ip('me').latlng}\n')

def create_account(username):
    # Implement account creation functionality
    if username not in users:
        users[username] = []
        return 'Account created successfully'
    return 'Username already in use'

def view_urls(username):
    # Implement functionality for viewing all shortened URLs
    if username in users:
        return users[username]
    return 'User not found'

def edit_url(old_url, new_url, username):
    # Implement functionality for editing shortened URLs
    if username in users and old_url in users[username]:
        users[username].remove(old_url)
        users[username].append(new_url)
        return 'URL edited successfully'
    return 'URL not found or user not authorized'

def delete_url(url, username):
    # Implement functionality for deleting shortened URLs
    if username in users and url in users[username]:
        users[username].remove(url)
        return 'URL deleted successfully'
    return 'URL not found or user not authorized'

def view_analytics(username):
    # Implement functionality for viewing analytics for all shortened URLs
    if username in users:
        return {url: get_clicks(url) for url in users[username]}
    return 'User not found'

def get_clicks(short_url):
    # Helper function for getting the number of clicks for a shortened URL
    with open('analytics.txt', 'r') as f:
        return len([line for line in f if line.split()[0] == short_url])

def view_all_urls():
    # Implement functionality for viewing all shortened URLs
    with open('url_database.txt', 'r') as f:
        return [line.split()[0] for line in f]

def delete_user(username):
    # Implement functionality for deleting user accounts
    if username in users:
        del users[username]
        return 'User deleted successfully'
    return 'User not found'

def view_system_performance():
    # Implement functionality for monitoring system performance and analytics
    return {'Total URLs': len(view_all_urls()), 'Total Users': len(users), 'Total Clicks': sum(get_clicks(url) for url in view_all_urls())}