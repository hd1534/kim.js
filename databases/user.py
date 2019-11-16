from ..app import DB
import hashlib
import base64
import datetime
import enum


class User(DB.Model):
    __tablename__ = 'user'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)
    id = DB.Column(DB.String(50), nullable=False)
    password = DB.Column(DB.String(50), nullable=False)
    name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(50), nullable=True)
    created_date = DB.Column(DB.DateTime, default=datetime.datetime.now)

    #
    # student = DB.relationship("Student", uselist=False, back_populates="user")
    #
    # afterschool_request = DB.relationship('AfterschoolRequest',
    #                                       back_populates='user')
    # assignments = DB.relationship('Assignment', back_populates='assignor')
    # reports = DB.relationship('Report', back_populates='author')
    # circle = DB.relationship("Circle", uselist=False, back_populates="chair")
    # circle_request = DB.relationship("CircleRequest", back_populates="user")
    # ingang_request = DB.relationship('IngangRequest', back_populates='user')
    # ingang_black_list = DB.relationship('IngangBlackList',
    #                                     back_populates='user')
    # ingang_black_list_log = DB.relationship('IngangBlackListLog',
    #                                         back_populates='user')
    # dets_request = DB.relationship('DetsRequest', back_populates='user')
    # counsel_request = DB.relationship('CounselRequest', back_populates='user')
    # mentoring_request = DB.relationship('MentoringRequest',
    #                                     back_populates='user')
    # mentor = DB.relationship('Mentor', back_populates='teacher')
    # mentoring_black_list = DB.relationship(
    #     'MentoringBlackList', back_populates='user')
    # book = DB.relationship('Book', back_populates='student')
    # rank = DB.relationship('Rank', back_populates='user')
    # push_registerid = DB.relationship('PushRegisterId', back_populates='user')
    # sns_pages = DB.relationship('SnsPages', back_populates='boss')
    # sns_posts = DB.relationship('SnsPosts', back_populates='writer')
    # sns_postimage = DB.relationship('SnsPostImage', back_populates='writer')
    # sns_comment = DB.relationship('SnsComment', back_populates='writer')
    # sns_permission = DB.relationship('SnsPermission', back_populates='user')
    # sport_member = DB.relationship('SportMember', back_populates='user')
    #
    # etc_requester = DB.relationship('EtcRequest', back_populates='user')
    # etc_application = DB.relationship('EtcApplication', back_populates='host')
    #
    # echo_posts_writer = DB.relationship('EchoPosts', back_populates='writer')
    # echo_user_tags = DB.relationship('EchoUserTags', back_populates='user')
    # echo_comment_writer = DB.relationship(
    #     'EchoComment', back_populates='writer')
    # echo_tags_owner = DB.relationship('EchoTags', back_populates='owner')


def get_user(user_idx):
    return User.query.filter_by(idx=user_idx).first()


def get_all_user_by_name(user_name):
    return User.query.filter_by(name=user_name).all()


def add_user(user_data):
    DB.session.add(
        User(
            name=user_data['name'],
            id=user_data['id'],
            password=base64.b64encode(
                hashlib.sha256(str.encode(user_data['password'])).digest()),
            email=user_data['email']
        )
    )
    DB.session.commit()
