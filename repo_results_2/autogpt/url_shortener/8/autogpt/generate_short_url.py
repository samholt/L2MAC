import string
import random
import json

def generate_short_url(custom_short_url=None):
    if custom_short_url:
        with open('urls.json', 'r') as file:
            data = json.load(file)
            if custom_short_url in data:
                return 'This short link is already in use.'
            else:
                return custom_short_url
    else:
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url