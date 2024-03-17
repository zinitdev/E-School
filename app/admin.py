from app import app, db
from app.models import Grade, Class, Student, Score, Subject, Test, Semester, AcademicYear
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app=app, name="E-School Administrator", template_mode='bootstrap4')


class GradeView(ModelView):
    column_list = ["id", "name", "classes"]


class ClassView(ModelView):
    column_list = ["id", "name", "grade", "students"]


class StudentView(ModelView):
    column_list = ["id", "first_name", "last_name", "class"]


class SubjectView(ModelView):
    column_list = ["id", "title", "scores", "semesters"]


class ScoreView(ModelView):
    column_list = ["id", "student", "subject", "result"]


class TestView(ModelView):
    column_list = ["id", "name", "scores"]


class SemesterView(ModelView):
    column_list = ["id", "name", "academic_year"]


class AcademicYearView(ModelView):
    column_list = ["id", "start_year", "end_year", "semesters"]
    

admin.add_view(GradeView(Grade, db.session))
admin.add_view(ClassView(Class, db.session))
admin.add_view(StudentView(Student, db.session))
admin.add_view(SubjectView(Subject, db.session))
admin.add_view(ScoreView(Score, db.session))
admin.add_view(TestView(Test, db.session))
admin.add_view(SemesterView(Semester, db.session))
admin.add_view(AcademicYearView(AcademicYear, db.session))