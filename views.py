import datetime
from datetime import date
from datetime import time
import time
from flask import Blueprint, jsonify, redirect, render_template, request, flash, jsonify, session, url_for
from flask_login import login_required, current_user
import json
import mysql.connector
from pymysql import NULL
from .models import data1
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def sendDB():
    print("logged in")
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='sis_point'
    )
    dbCon = mydb.cursor()
    # -------- User Info ------- #
    dbCon.execute("SELECT * FROM students")
    students= dbCon.fetchall()
    for i in students:
        if i[4] == session['user']:
            student_name = i[5] +" " + i[6]
            ids = i[4]
            student_departman= i[1]
            grades = str(i[2]) + i[3]
    day =str(date.today())
    print(day)
    daily= datetime.datetime.strptime(day, "%Y-%m-%d")
    print(daily)
    dbCon=mydb.cursor()
    dbCon.execute("SELECT * FROM data1 WHERE DATE='"+day+"'")
    raw_data= dbCon.fetchall()
    dbCon.execute("SELECT * FROM activity")
    activity= dbCon.fetchall()
    print(activity)
    print(raw_data)
    ###### Daily ######
    point1= 0
    point2= 0
    point3= 0
    point4=0
    for i in raw_data:
        print("raw_data")
        for x in activity:
            print("activity")
            if i[3] == x[1]:
                print("point")
                if i[3] == 1:
                    act_1= i
                    point1 += act_1[4] * x[3]
                    print(point1)
                    #return render_template('index.html', puan1=point1)
                elif x[1] == 2:
                    act_2= i
                    point2+= act_2[4] * x[3]
                    print(point2)
                    #return render_template('index.html', puan2=point2)
                elif x[1] == 3:
                    act_3= i
                    point3+= act_3[4] * x[3]
                    print(point3)
                    #return render_template('index.html', puan3=point3)
                elif x[1] == 4:
                    act_4= i
                    point4+= act_4[4]
                    print(point4)
    ###### Weekly ######

    ###### Monthly ######
    return render_template('index.html', puan1=point1, puan2=point2, puan3=point3, puan4=point4, idim= ids , name= student_name , departman = student_departman , grade= grades )
                


@views.route('/hmredirect', methods=['GET', 'POST'])
def goHmredirect():
    return redirect(url_for('views.sendDB'))

@views.route('/add', methods=['GET', 'POST'])
def goAdd():
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='sis_point'
    )
    dbCon = mydb.cursor()
    dbCon.execute("SELECT * FROM students")
    students= dbCon.fetchall()
    for i in students:
        if i[4] == session['user']:
            student_name = i[5] +" " + i[6]
            ids = i[4]
            student_departman= i[1]
            grades = str(i[2]) + i[3]
    if request.method == 'POST':
        date = request.form.get('basicFlatpickr')
        kitap = request.form.get('txt2')
        cevsen = request.form.get('txt3')
        kk = request.form.get('txt') 
        print(kitap)
        print(cevsen)
        print(kk)
        print(date)
        teheccud=request.form.get('check1')
        print(teheccud)
        if kitap and cevsen and kk:
            dbCon.execute("SELECT id FROM `data1`")
            raw_data = dbCon.fetchall()
            user_id=session.values()
            values=list(user_id)
            student_id=values[-1]
            result=request.form.getlist("check1")
            if result:
                teheccud= 1
            new_data1 = data1(student_id=student_id,date=date, act_type=1, point=kitap)
            new_data2 = data1(student_id=student_id,date=date, act_type=2, point=cevsen)
            new_data3 = data1(student_id=student_id,date=date, act_type=3, point=kk)
            new_data4 = data1(student_id=student_id,date=date, act_type=4, point=teheccud)
            db.session.add(new_data1)
            db.session.commit()
            print("way anasi1")
            db.session.add(new_data2)
            db.session.commit()
            print("way anasi2")
            db.session.add(new_data3)
            db.session.commit()
            print("way anasi3")
            db.session.add(new_data4)
            print("way anasi3.5")
            try:
                db.session.commit()
                print("way anasi4")
                flash("Data updated!", category='success')
                time.sleep(1)
            except:
                print("no teheccud")
    return render_template('index2.html', user=current_user, idim= ids , name= student_name , departman = student_departman , grade= grades)

@views.route('/hmteacher', methods=['GET', 'POST'])
@login_required
def home_t():
    
    return render_template('index_t.html')

def update():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sis_point"
    )
    value=NULL
    act_type_point=NULL
        
    mycursor = mydb.cursor()

    sql = "UPDATE data1 SET point = '"+value+"' WHERE student_id ='"+session.values()+"' act_type = '"+act_type_point+"'"

    mycursor.execute(sql)

    mydb.commit()

@views.route('/pfsetting', methods=['GET', 'POST'])
def pfSetting():
    print("profile page")
    mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='sis_point'
    )
    dbCon=mydb.cursor()
    dbCon.execute("SELECT * FROM students")
    students= dbCon.fetchall()
    for i in students:
        if i[4] == session['user']:
            student_name = i[5] +" " + i[6]
            ids = i[4]
            student_departman= i[1]
            grades = str(i[2]) + i[3]
            return render_template('user_profile.html', idim= ids , name= student_name , departman = student_departman , grade= grades )


    return render_template('user_profile.html', user=current_user)
