from app import app, admin, dao
from flask import render_template, request


@app.context_processor
def utils_processor():
    return dict(categories=dao.load_grades(), 
                classes=dao.load_classes())


@app.route('/')
def home():
    return render_template('pages/index.html')


@app.route('/grades/<int:grade_id>')
def details(grade_id):
    return render_template('pages/details.html', grade=dao.load_grade(grade_id))


@app.route('/class/<int:class_id>')
def class_details(class_id):
    return render_template('pages/class-details.html', class_details=dao.load_class(class_id))


@app.route('/students')
def students():
    return render_template('pages/students.html', students=dao.load_students(keyword=request.args.get('keyword')))