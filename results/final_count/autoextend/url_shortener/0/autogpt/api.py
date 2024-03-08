from flask import Flask, request, jsonify, redirect
from url_shortener import URLShortener
from database import Database

app = Flask(__name__)
url_shortener = URLShortener()
database = Database()


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json['url']
    shortened_url = database.get_shortened_url(original_url)
    if not shortened_url:
        shortened_url = url_shortener.shorten_url(original_url)
        database.store_url_mapping(original_url, shortened_url)
    return jsonify({'shortened_url': shortened_url})


@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url: str):
    original_url = database.get_original_url(shortened_url)
    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found', 404


if __name__ == '__main__':
    app.run()