from flask_restplus import Api
from flask import url_for
from setting import debug


@property
def specs_url(self):
    return url_for(self.endpoint('specs'), _external=True, _scheme='https')


# Only for production mode
if debug is False:
    Api.specs_url = specs_url

api = Api(
    title='Knock',
    version='1.0',
    description="KIM.JS project Knock"
)


def api_loader(*name_spaces):
    for name_space in name_spaces:
        api.add_namespace(__import__('api.' + name_space, fromlist=[name_space]).ns)


api_loader(
    'user'
)

