import mysql.connector

connection = mysql.connector.connect(host="localhost", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    something = cursor.fetchall()
    for row in something:
        print(row)
finally:
    connection.close()
