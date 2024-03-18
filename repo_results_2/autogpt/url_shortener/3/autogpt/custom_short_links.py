def assign_custom_short_link(url, custom_link):
    urls = read_file('urls.json')
    if custom_link not in urls.values():
        urls[url] = custom_link
        write_to_file('urls.json', urls)
    else:
        raise Exception('Custom short link is already in use.')