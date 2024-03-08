from flask import Flask, request, jsonify
from url_shortener import URLShortener

app = Flask(__name__)
url_shortener = URLShortener()


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('original_url')
    if original_url:
        short_url = url_shortener.shorten_url(original_url)
        return jsonify({'short_url': short_url})
    else:
        return jsonify({'error': 'Invalid request'}), 400


@app.route('/<short_url>', methods=['GET'])
def get_original_url(short_url):
    try:
        original_url = url_shortener.get_original_url(short_url)
        return jsonify({'original_url': original_url})
    except KeyError:
        return jsonify({'error': 'Short URL not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)