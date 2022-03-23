import mysql.connector
bd= mysql.connector.connect(
    host="localhost",
    user="root",
    password="demeter1",
    database="primeirobanco"

)

bd_cursor=bd.cursor()
bd_cursor.execute("CREATE DATABASE primeirobanco")