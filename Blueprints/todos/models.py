from email.headerregistry import ParameterizedMIMEHeader
from tkinter import N
from Blueprints.app import db

class Todo(db.Model):
    __tablename__ = 'todos'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, Nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<TODO {self.title}, Done: {self.done}>"

    def get_id(self):
        return self.tid
