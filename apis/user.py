from flask import request
from flask_restplus import (
    Namespace,
    Resource,
    fields,
    marshal
)
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import jwt_required, get_jwt_identity

from databases.user import (
    add_user,
    get_user,
    get_all_user,
    get_user_by_id_pass,
    change_password,
    delete_user
)

ns = Namespace('user', description='User methods')

# bookmark_full_model = ns.model('BookmarkFullModel', {
#     'idx': fields.Integer(required=True),
#
# })

# recent_full_model = ns.model('RecentFullModel', {
#     'idx': fields.Integer(required=True),
#
# })

user_full_model = ns.model('UserFullModel', {
    'idx': fields.Integer(required=True),
    'id': fields.String(required=True),
    'password': fields.String(required=True),  # 나중에 지울거
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'type': fields.String(required=True),
    'created_date': fields.DateTime(required=True)
    # 'bookmarks': fields.List(fields.Nested()),
    # 'recent': fields.List(fields.Nested())
})

user_full_list_model = ns.model('UserFullListModel', {
    'users': fields.List(fields.Nested(user_full_model))
})

sign_up_model = ns.model('SignUpModel', {
    'id': fields.String(required=True),
    'password': fields.String(required=True),
    'name': fields.String(required=True),
    'email': fields.String()
})

sign_in_model = ns.model('SignInModel', {
    'id': fields.String(required=True),
    'password': fields.String(required=True)
})

password_change_model = ns.model('PasswordChangeModel', {
    'old_password': fields.String(required=True),
    'new_password': fields.String(required=True)
})


@ns.route('/')
class UserResource(Resource):

    @ns.marshal_with(user_full_list_model)
    @ns.doc(description='''모든 사용자의 정보를 출력한다''',
            responses={200: '모든 사용자 정보를 성공적으로 출력했습니다.'})
    def get(self):
        return get_all_user()


@ns.route('/sign_in')
class SignInResource(Resource):

    # 추후 세션이나 쿠키로 (아마도 세션으로) 할듯
    @ns.expect(sign_in_model)
    @ns.marshal_with(user_full_model)
    @ns.doc(responses={200: '성공', 403: '가격을 숫자로 입력해 주세요'},
            description='''로그인을 합니다. 성공시 정보를 줍니다.''')
    def post(self):
        data = request.get_json()
        get_user_by_id_pass(data['id'], data['password'])
        return {}, 200


@ns.route('/<user_idx>')
class UserIdxResource(Resource):

    @ns.marshal_with(user_full_model)
    @ns.doc(description='''user_idx 로 사용자의 정보를 출력한다''',
            responses={200: '사용자 정보를 성공적으로 출력했습니다.',
                       404: '없는 유저 입니다.'})
    def get(self, user_idx):
        return get_user(user_idx)
