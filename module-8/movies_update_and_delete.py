import mysql.connector as sql

def show_films(cursor, title):
    cursor.execute('''
    SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    ''')
    films = cursor.fetchall()
    print("\n-- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))

def main():
    connection = sql.connect(
        host='127.0.0.1',
        user='root',
        password='Trunks!99',
        database='movies'
    )
    cursor = connection.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    insertQuery = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Star Wars', '2000', '155', 'George Lucas', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));"
    cursor.execute(insertQuery)
    connection.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    updateQuery = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien';"
    cursor.execute(updateQuery)
    connection.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    deleteQuery = "DELETE FROM film WHERE film_name = 'Gladiator';"
    cursor.execute(deleteQuery)
    connection.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    cursor.close()
    connection.close()

main()
