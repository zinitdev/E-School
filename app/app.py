from app import app, admin, dao
from flask import render_template


@app.route('/')
def home():
    return render_template('pages/index.html', 
                           categories=dao.load_grades(),
                           classes=dao.load_classes())