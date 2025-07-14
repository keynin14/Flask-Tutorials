from turtle import title
from flask import request, render_template, redirect, url_for, Blueprint

from Blueprints import people
from Blueprints.app import db
from Blueprints.blueprints.people.models import Person

people = Blueprint('todos',__name__,template_folder='templates')

@people.route('/')
def index():
    people = Person.query.all()
    return render_template('todos/index.html', people=people)

@people.route('/create', methods=['GET','POST'])
def create():
    if reqeuest.method == 'GET':
        return render_template('todos/create.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        job = request.form.get('job')
        done = True if 'done' in request.form.keys() else False

        job = job if job != '' else None


        person = Person(name=name, age=age, job=job)

        db.session.add(people)
        db.session.commit()

        return redirect(url_for('people.index'))
