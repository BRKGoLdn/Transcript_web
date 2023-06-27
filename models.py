from .__init__ import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    def get_id(self):
        return (self.student_id)

class data1(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True, unique=True)
    act_type = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, primary_key=True)
    point=db.Column(db.Integer, primary_key=True)
