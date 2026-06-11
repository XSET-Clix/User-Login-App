import mysql.connector
from flask import Flask, render_template, request
import re
app = Flask(__name__)
@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password= request.form['password']
        mydb = mysql.connector.connect(
        host="sql5.freesqldatabase.com",
        user="sql5830052",
        password="BsFMXidZhB",
        database="sql5830052",
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetail WHERE Name = %s AND Password = %s",(username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful!')
            return render_template('welcome.html',msg=msg,name=name, id=id)
        else:
            msg = 'incorrect Credentials. Kindly check'
            return render_template('login.html',msg=msg)
    else:
        return render_template('login.html')
@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = "Logged out successfully"
    return render_template('login.html',msg=msg,name=name,id=id)
@app.route('/register',methods=['GET','POST'])
def register():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mydb = mysql.connector.connect(
        host="sql5.freesqldatabase.com",
        user="sql5830052",
        password="BsFMXidZhB",
        database="sql5830052",
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s',(username, email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'^[^\d]*@[^\d]*\.\.[^\d]*$',email):
            msg = 'Invalid email address!'
        elif not username or not password or not email:
            msg = 'Kindly fill the details!'
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)', (username, password, email))
            mydb.commit()
            msg = 'Your Registration is Successful'
            name = username
            return render_template('welcome.html',msg=msg,name=name)
    elif request.method == 'POST':
        msg = 'Kindly fill the details!'
        return render_template('register.html',msg=msg)