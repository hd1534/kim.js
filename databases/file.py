from databases import DB
from sqlalchemy.sql import func
from setting import UPLOAD_FOLDER_PATH
from exceptions import CustomException
from upload import allowed_file, generate_file_hash
from databases.user import get_user
import os


class UploadFile(DB.Model):
    __tablename_ = 'upload_file'

    idx = DB.Column(DB.Integer, primary_key=True,
                    nullable=False, autoincrement=True)

    num = DB.Column(DB.Integer, nullable=False)  # 게시물내에서 번호? ex {1} 은 뭐고 {2}은 뭐다 면 {숫자} 에 매칭

    file_type = DB.Column(DB.String(20), nullable=False)

    uploader_idx = DB.Column(
        DB.Integer, DB.ForeignKey('user.idx'), nullable=False)
    uploader = DB.relationship('User', back_populates='upload_file')

    lecture_idx = DB.Column(DB.Integer, DB.ForeignKey('lecture.idx'), nullable=True)
    lecture = DB.relationship('Lecture', back_populates='files')

    # course_idx = DB.Column(DB.Integer, DB.ForeignKey('course.idx'), nullable=True)
    # course = DB.relationship('Course', back_populates='image')

    uploaded_date = DB.Column(DB.DateTime, server_default=func.now())

    hashed_filename = DB.Column(DB.Text, nullable=False)
    filename = DB.Column(DB.Text, nullable=False)


def get_uploaded_file_by_idx(idx):
    return UploadFile.query.filter_by(idx=idx).first()


def upload_file(file, uploader_idx, num):
    if file is None:
        raise CustomException("file is not founded", 400)

    if not allowed_file(file.filename):
        raise CustomException('file is not allowed', 403)

    user = get_user(uploader_idx)
    if user is None:
        raise CustomException("user is not founded", 404)

    hashed_filename = generate_file_hash(file.filename)
    try:
        file.save(os.path.join(UPLOAD_FOLDER_PATH, hashed_filename))
    except Exception as e:
        print(e)
        # print(str(e))
        raise CustomException("an error occurred when saving file", 500)

    DB.session.add(UploadFile(
        num=num,
        uploader_idx=uploader_idx,
        hashed_filename=hashed_filename,
        filename=file.filename,
        file_type=file.content_type
    ))
    DB.session.commit()

    return {}, 200


def update_uploaded_file(file, uploaded_file_idx):
    uploaded_file = UploadFile.query.filter_by(idx=uploaded_file_idx).first()
    if uploaded_file is None:
        raise CustomException("can't find that file", 404)

    hashed_old_filename = uploaded_file.hashed_filename
    hashed_filename = generate_file_hash(file.filename)

    try:
        file.save(os.path.join(UPLOAD_FOLDER_PATH, hashed_filename))
    except Exception as e:
        print(e)
        # print(str(e))
        raise CustomException("an error occurred when saving file", 500)

    uploaded_file.filename = file.filename
    uploaded_file.hashed_filename = hashed_filename
    DB.session.commit()

    try:
        os.remove(os.path.join(UPLOAD_FOLDER_PATH, hashed_old_filename))
    except Exception as e:
        print(e)
        print(str(e))
        # 지우는건 실패해도 상관 ㄴ

    return {}, 200


def delete_uploaded_file(uploaded_file_idx):
    uploaded_file = UploadFile.query.filter_by(idx=uploaded_file_idx).first()

    if uploaded_file is None:
        raise CustomException("can't find that file", 404)

    hashed_old_filename = uploaded_file.hashed_filename

    DB.session.delete(uploaded_file)
    DB.session.commit()

    try:
        os.remove(os.path.join(UPLOAD_FOLDER_PATH, hashed_old_filename))
    except Exception as e:
        print(e)
        print(str(e))
        # 지우는건 실패해도 상관 ㄴ

    return {}, 200
