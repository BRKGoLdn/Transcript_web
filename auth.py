from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import mysql.connector
from flask_login import LoginManager
from .models import User
from flask import Flask


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    global user
    if request.method == 'POST':
        mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='sis_point'
        )
        dbCon = mydb.cursor()
        student_id = request.form.get('username')
        student_id = int(student_id)
        dbCon.execute("select * from `user`")
        raw= dbCon.fetchall()
        rank = request.form.get('rank_select')
        print('this is the rank:', rank)
        for i in raw:
            if i[1] == student_id:
                user=i[1]
                session['user']= user
                user = User()
                flash("Logged in succesfully", category='success')
                login_user(user)
                login_user(user, remember=True)
                return redirect(url_for("views.sendDB"))
    return render_template("auth_login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))