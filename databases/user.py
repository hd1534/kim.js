from databases import DB
import hashlib
import base64
import datetime
from exceptions import (
    CustomException,
    NoPermissionException
)


def password_form_check(password):
    if len(password) < 9:
        raise CustomException("incorrect password form", 406)


class User(DB.Model):
    __tablename__ = 'user'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)
    id = DB.Column(DB.String(50), nullable=False)
    password = DB.Column(DB.String(50), nullable=False)
    name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(50), nullable=True)
    type = DB.Column(DB.Enum('admin', 'normal'), nullable=False, default='normal')
    created_date = DB.Column(DB.DateTime, nullable=False, default=datetime.datetime.now)

    # bookmark = DB.relationship('Bookmark', back_populates='user')
    # recent = DB.relationship('Recent', back_populates='user')


def add_user(user_data):
    password_form_check(user_data['password'])
    DB.session.add(
        User(
            id=user_data['id'],
            password=base64.b64encode(
                hashlib.sha256(str.encode(user_data['password'])).digest()),
            name=user_data['name'],
            email=user_data['email']
        )
    )
    DB.session.commit()
    return {}, 200


def get_user(user_idx):
    user = User.query.filter_by(idx=user_idx).first()
    if user is None:
        raise CustomException('no matched idx', 404)
    return user, 200


def get_all_user():
    return User.query.all(), 200


def get_user_by_id_pass(user_id, password):
    password_form_check(password)

    user = User.query.filter_by(id=user_id)
    if user.first() is None:
        raise CustomException("no matched id", 404)

    password = base64.b64encode(
        hashlib.sha256(str.encode(password)).digest())
    user.filter_by(password=password).first()

    if user is None:
        raise CustomException("incorrect password", 404)

    return user, 200


def change_password(user_idx, old_password, new_password):
    password_form_check(old_password)

    user = User.query.filter_by(idx=user_idx).first()
    if user is None:
        raise CustomException("user is not founded", 404)

    if user.password.encode() != base64.b64encode(
                hashlib.sha256(str.encode(old_password)).digest()):
        raise CustomException('old password is incorrect', 403)

    password_form_check(new_password)

    user.password = base64.b64encode(
                hashlib.sha256(str.encode(new_password)).digest())
    DB.session.commit()
    return {}, 200


def delete_user(user_idx, target_idx):
    if user_idx != target_idx:
        if get_user(user_idx).type != 'admin':
            raise NoPermissionException()

    target = User.query.filter_by(idx=user_idx).first()
    if target is None:
        raise CustomException("user is not founded", 404)

    DB.session.delete(target)
    DB.session.commit()
    return 200
