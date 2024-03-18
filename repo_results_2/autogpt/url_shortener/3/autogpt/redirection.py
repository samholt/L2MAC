def redirect(short_url):
    urls = read_file('urls.json')
    for url, short in urls.items():
        if short == short_url:
            return url
    raise Exception('Shortened URL does not exist.')