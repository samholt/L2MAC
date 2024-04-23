import random
import string
from datetime import datetime, timedelta

import requests
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "a_very_secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Mock database
urls_db = {}
users_db = {"admin": {"password": "admin", "urls": [], "is_admin": True}}
# Analytics database
analytics_db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if username in users_db:
        return jsonify({"error": "Username already exists"}), 400
    users_db[username] = {"password": password, "urls": []}
    return jsonify({"message": "User registered successfully"}), 200


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = users_db.get(username)
    if user and user["password"] == password:
        session["user"] = username
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
    return jsonify({"message": "Logged out successfully"}), 200


@app.route("/shorten", methods=["POST"])
def shorten_url():
    original_url = request.form["url"]
    expiration_date = request.form.get("expiration_date")
    if expiration_date:
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")
    else:
        expiration_date = datetime.now() + timedelta(days=365)  # Default expiration 1 year from now
    if validate_url(original_url):
        short_url = generate_short_url()
        urls_db[short_url] = {"url": original_url, "expiration": expiration_date}
        if "user" in session:
            users_db[session["user"]]["urls"].append(short_url)
        # Initialize analytics for the new short URL
        analytics_db[short_url] = {"clicks": 0, "click_details": []}
        return (
            jsonify(
                {
                    "original_url": original_url,
                    "short_url": short_url,
                    "expiration_date": expiration_date.strftime("%Y-%m-%d %H:%M:%S"),
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Invalid URL"}), 400


@app.route("/<short_url>")
def redirect_to_original(short_url):
    if short_url in urls_db and datetime.now() <= urls_db[short_url]["expiration"]:
        # Update analytics
        update_analytics(short_url, request.remote_addr)
        return redirect(urls_db[short_url]["url"])
    elif short_url in urls_db and datetime.now() > urls_db[short_url]["expiration"]:
        return jsonify({"error": "URL has expired"}), 410
    else:
        return jsonify({"error": "URL not found"}), 404


@app.route("/analytics/<short_url>")
def view_analytics(short_url):
    if short_url in analytics_db:
        return jsonify(analytics_db[short_url]), 200
    else:
        return jsonify({"error": "Analytics not found for the given URL"}), 404


@app.route("/user/urls")
def user_urls():
    if "user" in session:
        user_urls = users_db[session["user"]]["urls"]
        return jsonify({"urls": user_urls}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/user/edit/<short_url>", methods=["POST"])
def edit_url(short_url):
    if "user" in session and short_url in users_db[session["user"]]["urls"]:
        new_url = request.form["url"]
        if validate_url(new_url):
            urls_db[short_url] = new_url
            return jsonify({"message": "URL updated successfully"}), 200
        else:
            return jsonify({"error": "Invalid URL"}), 400
    else:
        return jsonify({"error": "Unauthorized or URL not found"}), 401


@app.route("/user/delete/<short_url>", methods=["DELETE"])
def delete_url(short_url):
    if "user" in session and short_url in users_db[session["user"]]["urls"]:
        users_db[session["user"]]["urls"].remove(short_url)
        urls_db.pop(short_url, None)
        analytics_db.pop(short_url, None)
        return jsonify({"message": "URL deleted successfully"}), 200
    else:
        return jsonify({"error": "Unauthorized or URL not found"}), 401


# Admin routes
@app.route("/admin/urls")
def admin_view_urls():
    if "user" in session and users_db.get(session["user"], {}).get("is_admin", False):
        return jsonify({"urls": list(urls_db.keys())}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/admin/delete/url/<short_url>", methods=["DELETE"])
def admin_delete_url(short_url):
    if "user" in session and users_db.get(session["user"], {}).get("is_admin", False):
        urls_db.pop(short_url, None)
        analytics_db.pop(short_url, None)
        return jsonify({"message": "URL deleted successfully"}), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/admin/delete/user/<username>", methods=["DELETE"])
def admin_delete_user(username):
    if "user" in session and users_db.get(session["user"], {}).get("is_admin", False):
        if username in users_db:
            del users_db[username]
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Unauthorized"}), 401


def validate_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException:
        return False


def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = "".join(random.choice(characters) for _ in range(length))
    while short_url in urls_db:
        short_url = "".join(random.choice(characters) for _ in range(length))
    return short_url


def update_analytics(short_url, ip_address):
    analytics_db[short_url]["clicks"] += 1
    click_detail = {"timestamp": datetime.now().isoformat(), "ip_address": ip_address}
    analytics_db[short_url]["click_details"].append(click_detail)


if __name__ == "__main__":
    app.run(debug=True)
