from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

DB_NAME = 'knock'
DB_USER = 'root'
DB_PASSWORD = 'qwerty123'
DB_ADDRESS = '35.221.70.78:3306'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'\
    .format(DB_USER, DB_PASSWORD, DB_ADDRESS, DB_NAME)

DB = SQLAlchemy(app)
migrate = Migrate(app, DB)


@app.route("/")
def hello():
    return "Hello kim.js!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
