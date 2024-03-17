from app.models import Grade, Class, Student
from app import db

def load_grades():
    return Grade.query.filter(Grade.active.__eq__(True)).all()


def load_classes():
    return Class.query.filter(Class.active.__eq__(True)).all()


def load_students(class_id=None):
    data = db.session.query(Student.id, Student.first_name)\
                     .join(Class, Class.id.__eq__(Student.id))\
                     .group_by(Student.id)

    if class_id:
        data = data.having(Class.id.__eq__(class_id))

    return data.all()
