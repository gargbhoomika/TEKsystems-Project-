import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def queries_show():
    try:
        connection = mysql.connector.connect(host='localhost',database='teksystems',user='root',password='Bhoomi13@')
        sql_select_query = """Select * from userqueries"""
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        result = cursor.fetchall()
        connection.commit()
        return result
    except:
        return null
