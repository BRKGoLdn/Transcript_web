from flask import Blueprint, jsonify, redirect, render_template, request, flash, jsonify, session, url_for
from flask_login import login_required, current_user
import json
import mysql.connector
from pymysql import NULL

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def index():
    print("logged in")
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='sis_transcript'
    )
    dbCon = mydb.cursor()
    dbCon.execute("Select * from `students`")
    students=dbCon.fetchall()
    search= request.form.get('search')
    print(search)
    for i in students:
        print(i)
        if i[1] == search:
            print(i)
    return render_template('index.html', user=current_user)


@views.route('/setting', methods=['GET','POST'])
def setting():
    return render_template('setting.html')


@views.route('/transcript', methods=['GET','POST'])
def transcript():
    return render_template('transcript.html')