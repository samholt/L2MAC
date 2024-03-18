def track_click(short_url, location):
    urls = read_file('urls.json')
    for url, data in urls.items():
        if data['short'] == short_url:
            data['clicks'].append({'time': datetime.now(), 'location': location})
            write_to_file('urls.json', urls)
            break