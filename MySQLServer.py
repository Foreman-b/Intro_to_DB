import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass


try:
    with connect(
        host = "localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        ) as connection:
        create_database = "CREATE DATABASE IF NOT EXISTS alx_book_store;"

        with connection.cursor() as cursor:
            cursor.execute(create_database)
            connection.commit()
            print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(e)

connection.close()


