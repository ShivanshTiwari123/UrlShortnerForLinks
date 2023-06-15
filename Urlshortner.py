from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store long and short URLs
url_mapping = {}

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

# Home page
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortener</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }

            h1 {
                color: #333;
                text-align: center;
                margin-top: 40px;
            }

            form {
                max-width: 400px;
                margin: 40px auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 4px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            }

            input[type="text"] {
                width: 100%;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                margin-bottom: 10px;
            }

            button[type="submit"] {
                background-color: #4CAF50;
                color: #fff;
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            button[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>URL Shortener</h1>
        <form action="/shorten" method="post">
            <input type="text" name="url" placeholder="Enter a long URL" required>
            <button type="submit">Shorten</button>
        </form>
    </body>
    </html>
    """

# URL shortening
@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    shortened_url = request.host_url + short_url
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortened</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }}

            h1 {{
                color: #333;
                text-align: center;
                margin-top: 40px;
            }}

            .short-url-container {{
                max-width: 400px;
                margin: 40px auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 4px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            }}

            .short-url {{
                color: #333;
                font-size: 18px;
                text-align: center;
                word-break: break-all;
            }}
        </style>
    </head>
    <body>
        <h1>Shortened URL:</h1>
        <div class="short-url-container">
            <p class="short-url"><a href="{shortened_url}">{shortened_url}</a></p>
        </div>
    </body>
    </html>
    """

# Redirecting to the long URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Invalid short URL"

if __name__ == '__main__':
    app.run()
