from databases import DB
from sqlalchemy.sql import func
from exceptions import CustomException
from databases.user import get_user
from databases.tags import get_tag_by_idx
import os


class Course(DB.Model):
    __tablename_ = 'course'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)

    title = DB.Column(DB.String(100), nullable=False)
    description = DB.Column(DB.String(200), nullable=False)

    tag_idx = DB.Column(
        DB.Integer, DB.ForeignKey('tag.idx'), nullable=False)
    tag = DB.relationship('Tag', back_populates='course')

    # image_idx = DB.Column(DB.Integer, DB.ForeignKey('upload_file.idx'), nullable=True)
    # image = DB.relationship('UploadFile', back_populates='course')

    lecture = DB.relationship('Lecture', back_populates='course')

    uploaded_date = DB.Column(DB.DateTime, server_default=func.now())

    # comment = DB.relationship('Comment', back_populates='Course')


def get_uploaded_course_by_idx(idx):
    return Course.query.filter_by(idx=idx).first()


def get_all_uploaded_courses():
    return Course.query.all()


def upload_course(course, uploader_idx):
    if course is None:
        raise CustomException("course is not founded", 400)

    user = get_user(uploader_idx)
    if user is None:
        raise CustomException("user is not founded", 404)

    DB.session.add(Course(
        title=course['title'],
        description=['description'],
        tag_idx=course['tag_idx']
    ))
    DB.session.commit()

    return {}, 200


def update_uploaded_course(course, course_idx):
    if course is None:
        raise CustomException("course is not founded", 400)

    uploaded_course = Course.query.filter_by(idx=course_idx).first()
    if course is None:
        raise CustomException("uploaded course is not founded", 404)

    tag = get_tag_by_idx(course['tag_idx'])
    if tag is None:
        raise CustomException("Tag not 0found")

    uploaded_course.title = course['title']
    uploaded_course.description = course['description']
    uploaded_course.tag_idx = course['tag_idx']
    DB.session.commit()
    return {}, 200


def delete_uploaded_course(course_idx):
    uploaded_course = Course.query.filter_by(idx=course_idx).first()

    if uploaded_course is None:
        raise CustomException("can't find that course", 404)

    # TODO 강의 올리는 사람인지 체크

    DB.session.delete(uploaded_course)
    DB.session.commit()
    return {}, 200
