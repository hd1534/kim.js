from .import DB
import datetime
import enum


class Bookmark(DB.Model):
    __tablename__ = 'bookmark'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)
    id = DB.Column(DB.String(50), nullable=False)
    password = DB.Column(DB.String(50), nullable=False)
    name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(50), nullable=True)
    created_date = DB.Column(DB.DateTime, default=datetime.datetime.now)

    bookmark_idx = DB.Column(
        DB.Integer, DB.ForeignKey('bookmark.idx'), nullable=True)
    bookmark = DB.relationship('Bookmark', back_populates='user')


################################################################################


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
    return 200, User.query.filter_by(idx=user_idx).first()


def get_user_by_id_pass(id, password):
    user = User.query.filter_by(id=id)
    if user.first() is None:
        return 404, "no matched id"

    password = base64.b64encode(
        hashlib.sha256(str.encode(password)).digest())
    user.filter_by(password=password).first()

    if user is None:
        return 404, "incorrect password"

    return 200, user


def change_password(user_idx, old_pass, new_pass):
    user = User.query.filter_by(idx=user_idx).first()
    if user is None:
        return 404

    if user.password != base64.b64encode(
            hashlib.sha256(str.encode(old_pass)).digest()):
        return 403

    if password_form_check(new_pass):
        return 406

    user.password = base64.b64encode(
        hashlib.sha256(str.encode(new_pass)).digest())
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

