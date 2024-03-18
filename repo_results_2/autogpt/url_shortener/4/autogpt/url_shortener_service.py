import url_validation
import url_shortener
import json


def create_short_url(original_url):
    if url_validation.validate_url(original_url):
        short_url = url_shortener.generate_short_url()
        with open('urls.json', 'r+') as file:
            data = json.load(file)
            data.append({'original_url': original_url, 'short_url': short_url})
            file.seek(0)
            json.dump(data, file)
        return short_url
    else:
        raise ValueError('Invalid URL')