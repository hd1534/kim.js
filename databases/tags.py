from databases import DB
from datetime import datetime

from sqlalchemy import exc, or_


class Tag(DB.Model):
    __tablename__ = 'tag'

    idx = DB.Column(DB.Integer(), primary_key=True,
                    nullable=False, autoincrement=True)

    name = DB.Column(DB.String(20), nullable=False)

    description = DB.Column(DB.Text(), nullable=False)

    course = DB.relationship('Course', back_populates='tag')


def add_tag(tag_data):
    DB.session.add(Tag(
        name=tag_data['name'],
        description=tag_data['description']
    ))
    DB.session.commit()


def get_tag_by_idx(tag_idx):
    tag = Tag.query.filter_by(idx=tag_idx).first()
    if tag is None:
        return 404
    return tag


def get_all_tags():
    return Tag.query.all()


def search_tags_by_description(word):
    return Tag.query.\
        filter(or_(Tag.description.like('%'+word+'%'),
                   Tag.name.like('%'+word+'%'))).all()


def delete_tags_by_idx(tag_idx, user_idx):
    tag = Tag.query.filter_by(idx=tag_idx).first()
    if tag is None:
        return 404

    try:
        DB.session.delete(tag)
        DB.session.commit()
    except exc.IntegrityError:
        DB.session.rollback()
        return 409

    return 200
