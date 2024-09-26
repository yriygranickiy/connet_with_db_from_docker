
import psycopg2


def connection_db():
    print(f"Connecting to database...")

    print("_____________________________________________________________________")

    connection = psycopg2.connect(database="my_db", user="my_user", password="qwerty", host="localhost", port="5438")

    return connection
