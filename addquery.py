import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def queryaddition(username,userquery):
    try:
        connection = mysql.connector.connect(host='localhost', database='teksystems', user='root', password='Bhoomi13@')
        cur = connection.cursor()
        insertquery = "Insert into userqueries (username,query) values (%s,%s)"
        cur.execute(insertquery,(username,userquery,))
        connection.commit()
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
