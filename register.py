import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def registeruser(name,email,username,password):
    try:
        connection = mysql.connector.connect(host='localhost', database='teksystems', user='root', password='Bhoomi13@')
        cur = connection.cursor()
        insertquery = "INSERT INTO users (name,email,username,password) VALUES (%s, %s, %s, %s)"
        cur.execute(insertquery, (name,email,username,password,))
        connection.commit()
    except:
        connection.commit()
