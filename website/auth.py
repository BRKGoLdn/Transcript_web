from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import mysql.connector
from flask_login import LoginManager
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
        database='sis_transcript'
        )
        dbCon = mydb.cursor()
        email = request.form.get('email')
        print("Email alindi")
        password = request.form.get('password')
        print("password alindi")
        dbCon.execute("Select * from `users`")
        users=dbCon.fetchall()
        for i in users:
            if email == i[1]:
                print("Email dogrulandi")
                if password == i[4]:
                    print("Password dogrulandi")
                    flash("Login Succesfully", category='success')
                    return redirect(url_for('views.index'))
                else:
                    return render_template('login.html')


    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))