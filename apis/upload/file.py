from flask import request, abort, send_file, make_response
from flask_restplus import Resource, fields, marshal, Namespace
# from flask_jwt_extended import jwt_required, get_jwt_identity

from werkzeug.datastructures import FileStorage
from werkzeug import secure_filename

# from decorators import permission_required
from databases.upload.file import (
    get_uploaded_file_by_idx,
    upload_file,
    update_uploaded_file,
    delete_uploaded_file
)

from datetime import datetime
from random import random
import os
import io
import zipfile
import hashlib
import urllib
import time


ns = Namespace('file', description='File methods')


@ns.route('/')
class FileResource(Resource):
    # @jwt_required TODO
    @ns.param('file', description='File',
              _in='formData', type='file', required=True)
    @ns.doc(description='''파일을 업로드 합니다.''',
            responses={204: '정상적으로 업로드 되었습니다.',
                       400: '제출된 파일을 찾을 수 없습니다. 다시 확인해 주십시오.',
                       403: '''제출된 파일에 문제가 있습니다.
                               허가되지 않은 파일을 업로드 하지는 않았는지
                               확인해 주십시오.''',
                       404: "없는 유저 입니다!"})
    def post(self):
        uploader_idx = 3  # TODO get_jwt_identity()[0]['idx']
        num = 1  # TODO request.get_json()['num']
        return upload_file(request.files.get('file'), uploader_idx, num)


@ns.route('/<int:file_idx>')
class FileIdxResource(Resource):
    @ns.doc(description='''파일을 수정 합니다.''',
            responses={204: '정상적으로 수정되었습니다.',
                       400: '파일을 찾을 수 없습니다. 다시 확인해 주십시오.',
                       403: '''제출된 파일에 문제가 있습니다.
                               허가되지 않은 파일을 업로드 하지는 않았는지
                               확인해 주십시오.''',
                       404: '''수정하려는 파일이 없거나, 없는 사용자 입니다.'''})
    @ns.param('file', description='Report Content',
              _in='formData', type='file', required=True)
    def put(self, file_idx):
        # user_idx = get_jwt_identity()[0]['idx']

        return update_uploaded_file(request.files.get('file'), file_idx)

    @ns.doc(description='''파일을 삭제 합니다.''',
            responses={204: '정상적으로 삭제 되었습니다.',
                       404: '''수정하려는 파일이 없거나, 없는 사용자 입니다.'''})
    def delete(self, file_idx):
        # user_idx = get_jwt_identity()[0]['idx']

        return delete_uploaded_file(file_idx), 204
