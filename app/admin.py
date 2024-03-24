import os.path as op
from app import app, db
from flask import redirect
from app.models import Grade, Class, Student, Score, Subject, Test, Semester, AcademicYear, RoleEnum
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_login import current_user, logout_user

path = op.join(op.dirname(__file__), 'static')
admin = Admin(app=app, name="E-School Administrator", template_mode='bootstrap4')

class ESchoolModelView(ModelView):
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    page_size = 10

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()


class GradeView(ESchoolModelView):
    column_list = ["id", "name", "classes"]


class ClassView(ESchoolModelView):
    column_list = ["id", "name", "grade", "students"]


class StudentView(ESchoolModelView):
    column_list = ["id", "first_name", "last_name", "class"]


class SubjectView(ESchoolModelView):
    column_list = ["id", "title", "scores", "semesters"]


class ScoreView(ESchoolModelView):
    column_list = ["id", "student", "subject", "result"]


class TestView(ESchoolModelView):
    column_list = ["id", "name", "scores"]


class SemesterView(ESchoolModelView):
    column_list = ["id", "name", "academic_year"]


class AcademicYearView(ESchoolModelView):
    column_list = ["id", "start_year", "end_year", "semesters"]


class AuthBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()


class StatisticsView(AuthBaseView):
    @expose('/')
    def index(self):
        return self.render('admin/statistics.html')


class LogoutView(AuthBaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


class UploadFileView(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()


admin.add_view(GradeView(Grade, db.session, category="Management"))
admin.add_view(ClassView(Class, db.session, category="Management"))
admin.add_view(StudentView(Student, db.session, category="Management"))
admin.add_view(SubjectView(Subject, db.session, category="Management"))
admin.add_view(ScoreView(Score, db.session, category="Management"))
admin.add_view(TestView(Test, db.session, category="Management"))
admin.add_view(SemesterView(Semester, db.session, category="Management"))
admin.add_view(AcademicYearView(AcademicYear, db.session, category="Management"))
admin.add_view(StatisticsView(name='Statistics', endpoint='statistics'))
admin.add_view(LogoutView(name='Log Out', category="Settings"))
admin.add_view(UploadFileView(path, '/static/', name="Files", category="Settings"))