from apis import api
from jinja2 import TemplateNotFound
from exceptions import (
    NoPermissionException,
    CustomException
)

# debug 모드는 에러 핸들러가 안되고
# 디버그 모드가 아닐때만 핸들러가 작동하드라


@api.errorhandler(TemplateNotFound)
def permission_handler(error):
    return {'message': 'TemplateNotFound'}, 404


@api.errorhandler(NoPermissionException)
def permission_handler(error):
    return {'message': 'no permission'}, 403


@api.errorhandler(CustomException)
def custom_handler(error):
    message, code = error.args
    return {'message': message}, int(code)


@api.errorhandler
def default_error_handler(error):
    return {'message': str(error)}, getattr(error, 'code', 500)
