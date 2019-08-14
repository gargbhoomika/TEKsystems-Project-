import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def index(username,password):
    try:
        connection = mysql.connector.connect(host='localhost',database='teksystems',user='root',password='Bhoomi13@')
        cur = connection.cursor()
        sql_select_query = "SELECT username FROM users WHERE username = %s"
        temp = cur.execute(sql_select_query,(username,))
        connection.commit()
        sql_select_query = "SELECT password FROM users WHERE username = %s"
        pas = cur.execute(sql_select_query,(username,))
        connection.commit()
        return "fine"
    except:
        return "error"
