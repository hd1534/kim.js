from flask_restplus import Api, Resource
from flask import url_for
from flask_cors import CORS
from app import app

app.config['ERROR_INCLUDE_MESSAGE'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 30  # 캐시 컨트롤 시간을 30초로

CORS(app)


@property
def specs_url(self):
    return url_for(self.endpoint('specs'), _external=True, _scheme='https')


# Only for production mode
if app.debug is False:
    Api.specs_url = specs_url

api = Api(
    app,
    title='Knock',
    version='1.0',
    description="KIM.JS project Knock"
)

__import__('resources.user')
