import mysql.connector
from mysql.connector import errorcode

# MySQL database configuration
config = {
    'user': 'root',
    'password': 'Trunks!99',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True
}
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    query = "SELECT * FROM studio"
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Studio RECORDS--")
    for row in result:
        print("Studio ID:", row[0])
        print("Studio Name:", row[1])
        print(" ")

    query = "SELECT * FROM genre"
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Genre RECORDS--")
    for row in result:
        print("Genre ID:", row[0])
        print("Genre Name:", row[1])
        print(" ")

    query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Short Film RECORDS--")
    for row in result:
        print("Film Name:", row[0])
        print("Runtime:", row[1])
        print(" ")

    query = "SELECT film_name, film_director FROM film ORDER BY film_director"
    cursor.execute(query)
    result = cursor.fetchall()
    print("--DISPLAYING Director RECORDS in Order--")
    for row in result:
        print("Film Name:", row[0])
        print("Director:", row[1])
        print(" ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()