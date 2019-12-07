from dimigoin.resource import api
from dimigoin.exceptions import NoPermissionException


@api.errorhandler(NoPermissionException)
def permission_handler(error):
    return {'message': 'no permission'}, 403


@api.errorhandler
def default_error_handler(error):
    return {'message': str(error)}, getattr(error, 'code', 500)
