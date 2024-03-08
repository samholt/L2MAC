class URLShortenerView:
    @staticmethod
    def display_short_url(short_url: str):
        print(f'Short URL: {short_url}')

    @staticmethod
    def display_error(error_message: str):
        print(f'Error: {error_message}')
