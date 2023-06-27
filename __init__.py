from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
import mysql.connector

db = SQLAlchemy()

def create_app():
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='sis_point'
    )
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = "python"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:@localhost/sis_point'
    db.init_app(app)

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, data1

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(student_id):
        try:
            user_id = session.values()
            values=list(user_id)
            student_id=values[-1]
            print(student_id)
            return User.query.get(int(student_id))
        except:
            print("none veri")


    return app