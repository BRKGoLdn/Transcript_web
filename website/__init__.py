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
    database='sis_transcript'
    )
    app = Flask(__name__, template_folder='templates')
    print("template found")
    app.config['SECRET_KEY'] = "python"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:@localhost/sis_transcript'
    db.init_app(app)
    print("db set")

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
