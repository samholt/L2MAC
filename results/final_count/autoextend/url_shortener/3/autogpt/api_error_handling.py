from flask import Flask, request, jsonify
from url_shortener import URLShortener

app = Flask(__name__)
url_shortener = URLShortener()


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('original_url')
    if original_url:
        try:
            short_url = url_shortener.shorten_url(original_url)
            return jsonify({'short_url': short_url})
        except ValueError:
            return jsonify({'error': 'Invalid URL'}), 400
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