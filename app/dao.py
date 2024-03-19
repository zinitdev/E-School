from app.models import Grade, Class, Student
from app import db


def load_grades():
    return Grade.query.filter(Grade.active.__eq__(True)).all()


def load_classes(grade_id=None):
    data = Class.query.filter(Class.active.__eq__(True))

    if grade_id:
        data = data.filter(Class.grade_id.__eq__(grade_id))
    
    return data.all()


def load_students(keyword=None, class_id=None):
    data = db.session.query(Student.id, Student.first_name, Student.last_name, Class.name)\
                    .join(Class.students)\
                    .group_by(Student.id)

    if keyword:
        data = data.filter(Student.first_name.contains(keyword))
        
    if class_id:
        data = data.having(Class.id.__eq__(class_id))

    return data.order_by(Student.first_name).all()


def load_grade(grade_id):
    return Grade.query.get_or_404(grade_id)


def load_class(class_id):
    return Class.query.get_or_404(class_id)