from databases import DB
from sqlalchemy.sql import func
from exceptions import CustomException
from databases.user import get_user
import os


class Lecture(DB.Model):
    __tablename__ = 'lecture'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)

    title = DB.Column(DB.String(100), nullable=False)
    description = DB.Column(DB.Text, nullable=False)

    course_idx = DB.Column(
        DB.Integer, DB.ForeignKey('course.idx'), nullable=False)
    course = DB.relationship('Course', back_populates='lecture')

    files = DB.relationship('UploadFile', back_populates='lecture')

    uploaded_date = DB.Column(DB.DateTime, server_default=func.now())

    # comment = DB.relationship('Comment', back_populates='Lecture')


def get_uploaded_lecture_by_idx(idx):
    return Lecture.query.filter_by(idx=idx).first()


def get_all_uploaded_lectures():
    return Lecture.query.all()


def upload_lecture(lecture, uploader_idx):
    if lecture is None:
        raise CustomException("lecture is not founded", 400)

    user = get_user(uploader_idx)
    if user is None:
        raise CustomException("user is not founded", 404)

    DB.session.add(Lecture(
        title=lecture['title'],
        description=['description']
    ))
    DB.session.commit()

    return {}, 200


def update_uploaded_lecture(lecture, lecture_idx):
    if lecture is None:
        raise CustomException("lecture is not founded", 400)

    uploaded_lecture = Lecture.query.filter_by(idx=lecture_idx).first()
    if lecture is None:
        raise CustomException("uploaded lecture is not founded", 404)

    uploaded_lecture.title = lecture['title']
    uploaded_lecture.description = lecture['description']
    DB.session.commit()
    return {}, 200


def delete_uploaded_lecture(lecture_idx):
    uploaded_lecture = Lecture.query.filter_by(idx=lecture_idx).first()

    if uploaded_lecture is None:
        raise CustomException("can't find that lecture", 404)

    # TODO 강의 올리는 사람인지 체크

    DB.session.delete(uploaded_lecture)
    DB.session.commit()
    return {}, 200
