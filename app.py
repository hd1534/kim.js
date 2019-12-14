from flask import Flask
from flask_migrate import Migrate
from apis import api
from setting import debug
from flask_cors import CORS
from databases import DB
from setting import (
    DB_USER,
    DB_PASSWORD,
    DB_ADDRESS,
    DB_NAME,
    MAX_CONTENT_LENGTH
)
from resources import register_blueprint

app = Flask(__name__)
api.init_app(app)
app.url_map.strict_slashes = False
app.config['ERROR_INCLUDE_MESSAGE'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 30  # 캐시 컨트롤 시간을 30초로
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'\
    .format(DB_USER, DB_PASSWORD, DB_ADDRESS, DB_NAME)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


__import__('handler')

CORS(app)
register_blueprint(app)
DB.init_app(app)
migrate = Migrate(app, DB)

if __name__ == "__main__":
    app.run(debug=debug, host='127.0.0.1', port=5000)
