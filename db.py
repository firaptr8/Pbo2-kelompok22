from mysql.connector import connect, Error

connection = None

try:

    connection = connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'jalan_kuy'
    )

except Error as err:
    print(err)