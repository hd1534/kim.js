from flask import Flask

app = Flask(__name__)

__import__('databases')
__import__('resources')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
