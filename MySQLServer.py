import mysql.connector
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

except mysql.connector.Error as e:
    print(e)

mycursor.close()
mydb.close()


