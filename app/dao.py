from app.models import Grade, Class, Student, User
from app import db


def load_users(user_id):
    return User.query.filter(User.active.__eq__(True)).first()


def load_user_by_email(email):
    return User.query.filter(User.email.contains(email)).first()


def load_user_by_username(username):
    return User.query.filter(User.username.contains(username)).first()


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


def create_user(data):
    user = User(**data)
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

    return user


def check_auth(data):
    user = User.query.filter(User.username.__eq__(data.get('username'))).first()
    if user and user.check_password(password=data.get('password')):
        return user
    return None