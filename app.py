from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

__import__('resources')
__import__('databases')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
