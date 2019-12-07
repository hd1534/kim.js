from flask import Flask
from api import api
from flask_cors import CORS

app = Flask(__name__)
api.init_app(app)
app.url_map.strict_slashes = False
app.config['ERROR_INCLUDE_MESSAGE'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 30  # 캐시 컨트롤 시간을 30초로

CORS(app)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
