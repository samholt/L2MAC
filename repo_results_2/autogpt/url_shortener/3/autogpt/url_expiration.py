def set_expiration(short_url, expiration):
    urls = read_file('urls.json')
    for url, data in urls.items():
        if data['short'] == short_url:
            data['expiration'] = expiration
            write_to_file('urls.json', urls)
            break

def check_expiration(short_url):
    urls = read_file('urls.json')
    for url, data in urls.items():
        if data['short'] == short_url:
            if datetime.now() > data['expiration']:
                raise Exception('URL has expired.')