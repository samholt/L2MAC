from url_shortener import URLShortener


def main():
    url_shortener = URLShortener()
    original_url = 'https://www.example.com'
    short_url = url_shortener.generate_short_url(original_url)
    print(f'Original URL: {original_url}')
    print(f'Short URL: {short_url}')
    retrieved_original_url = url_shortener.get_original_url(short_url)
    print(f'Retrieved Original URL: {retrieved_original_url}')


if __name__ == '__main__':
    main()