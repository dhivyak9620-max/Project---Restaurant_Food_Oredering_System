import mysql.connector


def connect_database():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your Paassword",
        database="restaurant_db"
    )

    return connection


def test_connection():

    try:

        connection = connect_database()

        if connection.is_connected():

            print("Database connection successful!")

        connection.close()

    except mysql.connector.Error as error:

        print("Database connection failed:", error)


if __name__ == "__main__":

    test_connection()