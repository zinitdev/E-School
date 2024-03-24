from app import app, admin, dao, login_manager, utils
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user


@app.context_processor
def utils_processor():
    return dict(categories=dao.load_grades(), 
                classes=dao.load_classes())


@login_manager.user_loader
def load_user(user_id):
    return dao.load_users(user_id)


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


@app.route('/admin/login', methods=['post'])
def login_admin():
    user = dao.check_auth(data={
        'username': request.form.get('username'), 
        'password': request.form.get('pwd')
    })

    if user and user.is_admin():
        flash("Login successful!", "success")
        login_user(user)

    flash("Login failed!", "error")

    return redirect('/admin')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # if dao.load_user_by_email(request.form.get('email')):
        #     flash('Email is already!', 'warning')
        #     return redirect(url_for('register'))

        if dao.load_user_by_username(request.form.get('username')):
            flash('Username is already!', 'warning')
            return redirect(url_for('register'))
        
        if dao.create_user(data={
            'username': request.form.get('username'),
            'password': request.form.get('pwd')
        }):
            flash('Successfully created', 'success')
            return redirect(url_for('home'))

        flash('Failed to create user', 'warning')
        
    return render_template('pages/register.html')