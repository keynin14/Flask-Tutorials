from flask import render_template, request 

from models import Person


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people=people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age = request.form.get('age')
            job = request.form.get('job')

            person= Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()
             
            people = Person.query.all()
            return render_template('index.html', people=people)

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        person = Person.query.get(pid)
        if person:
            db.session.delete(person)
            db.session.commit()
            return {'message': 'Person deleted successfully'}, 200
        else:
            return {'message': 'Person not found'}, 404

    
