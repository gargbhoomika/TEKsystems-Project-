from flask import Flask,request, render_template,redirect,url_for
import mysql.connector
from register import *
from login import index
from queries import queries_show
from edit import edituser
from emailsend import *
from addquery import queryaddition
from mysql.connector import Error
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/events', methods=['POST','GET'])
def events():
    return render_template('event.html')

@app.route('/updateprofile', methods=['POST','GET'])
def updateprofile():
    return render_template('update.html')

@app.route('/signuserup', methods=['POST','GET'])
def signuserup():
    return render_template('signup.html')

# @app.route('/queryshow')
def queryshow():
    result = queries_show()
    return render_template('queries.html',result=result)

@app.route('/signup/', methods=['POST','GET'])
def signup():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        registeruser(name,email,username,password)
        return render_template('login.html')
    else:
        return redirect(url_for('home'))

@app.route('/signin/', methods=['POST','GET'])
def signin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        x = index(username,password)
        result = queries_show()
        return render_template('queries.html',result=result)
    else:
        return redirect(url_for('home'))

@app.route('/updateuser/', methods=['POST','GET'])
def updateuser():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        edituser(name,email,username,password)
        result = queries_show()
        return render_template('queries.html',result=result)
    else:
        result = queries_show()
        return render_template('queries.html',result=result)

@app.route('/enquiry', methods=['POST','GET'])
def enquiry():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        try:
            connection = mysql.connector.connect(host='localhost',database='teksystems',user='root',password='Bhoomi13@')
            insertquery = """INSERT INTO usercontacts (name,email,subject,message) VALUES (%s,%s,%s,%s)"""
            cursor = connection.cursor()
            result = cursor.execute(insertquery,(name,email,subject,message))
            connection.commit()
            send_email(email,name)
            if connection.is_connected():
                cursor.close()
                connection.close()
            return render_template('success.html',name=name)
        except:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/queryadd', methods=['POST','GET'])
def queryadd():
    if request.method=='POST':
        username = request.form['username']
        query = request.form['query']
        queryaddition(username,query)
        result = queries_show()
        return render_template('queries.html',result=result)
    else:
        result = queries_show()
        return render_template('queries.html',result=result)

if __name__ == '__main__':
    app.run()
