import psycopg2
from psycopg2 import connect
from psycopg2._psycopg import OperationalError

import utils



#insert data in to database
def insert_into_db_list_users(cursor,list_users):
    insert_query = """
        Insert into users (id,username, email, password) 
        values (%s, %s, %s, %s)
    """
    try:
        for user in list_users:
            cursor.execute(insert_query, (user.id, user.username, user.email, user.password))
    except Exception as e:
        print(f"Error added data in database: {e}")

    print(f"{len(list_users)} users successfully added")
    print("_____________________________________________________________________")



def test_connection(list_users):
    print(f"Connecting to database...")
    print("_____________________________________________________________________")

    try:
        with psycopg2.connect(database="my_db", user="my_user", password="qwerty", host="localhost", port="5438") as conn:
            with conn.cursor() as cur:
                insert_into_db_list_users(cur, list_users)
                print("operation done successfully.........")
                print("_____________________________________________________________________")
                conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    except OperationalError as e:
        print(f"Connecting error : {e}")


