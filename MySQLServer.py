import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass


try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: ")
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    mydb.commit()
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(e)

mycursor.close()
mydb.close()


