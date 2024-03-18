import random
import string

def shorten_url(url):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))