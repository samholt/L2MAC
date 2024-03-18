from url_expiration import URLExpiration

expiration = URLExpiration()

def redirect(short_url):
    if expiration.is_expired(short_url):
        return 'Error: This URL has expired.'
    else:
        original_url = storage.get_original_url(short_url)
        if original_url is None:
            return 'Error: This short URL does not exist.'
        else:
            return 'Redirecting to ' + original_url