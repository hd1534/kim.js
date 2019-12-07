from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from setting import (
    DB_USER,
    DB_PASSWORD,
    DB_ADDRESS,
    DB_NAME
)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://{}:{}@{}/{}?charset=utf8mb4'\
    .format(DB_USER, DB_PASSWORD, DB_ADDRESS, DB_NAME)

DB = SQLAlchemy(app)
migrate = Migrate(app, DB)


__import__('databases.user')
