import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def edituser(name,email,username,password):
    try:
        connection = mysql.connector.connect(host='localhost', database='teksystems', user='root', password='Bhoomi13@')
        cur = connection.cursor()
        sql_update_query = "UPDATE users (name,email,username,password) set name = %s, email = %s, username = %s, password = %s";
        cur.execute(sql_update_query, (name,email,username,password,))
        connection.commit()
    except:
        connection.close()
