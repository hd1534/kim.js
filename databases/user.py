from databases import DB
import hashlib
import base64
import datetime


def password_form_check(password):
    return len(password) > 9


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
    if password_form_check(user_data['password']):
        return 406

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
    return 200


def get_user(user_idx):
    user = User.query.filter_by(idx=user_idx).first()
    if user is None:
        return 404, {'reason': 'no matched idx'}
    return 200, user


def get_all_user():
    return 200, {'users': User.query.all()}


def get_user_by_id_pass(id, password):
    user = User.query.filter_by(id=id)
    if user.first() is None:
        return 404, {'reason': "no matched id"}

    password = base64.b64encode(
        hashlib.sha256(str.encode(password)).digest())
    user.filter_by(password=password).first()

    if user is None:
        return 404, {'reason': "incorrect password"}

    return 200, user


def change_password(user_idx, old_password, new_password):
    user = User.query.filter_by(idx=user_idx).first()
    if user is None:
        return 404

    if user.password != base64.b64encode(
                hashlib.sha256(str.encode(old_password)).digest()):
        return 403

    if password_form_check(new_password):
        return 406

    user.password = base64.b64encode(
                hashlib.sha256(str.encode(new_password)).digest())
    DB.session.commit()
    return 200


def delete_user(user_idx, target_idx):
    if user_idx != target_idx:
        if get_user(user_idx).type != 'admin':
            return 403

    target = User.query.filter_by(idx=user_idx).first()
    if target is None:
        return 404

    DB.session.delete(target)
    DB.session.commit()
    return 200
