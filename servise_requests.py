import conection

con = conection.connection_db()

cur = con.cursor()
def insert_into_db_list_users(cursor, list_users):
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
    print("_____________________________________________________________________\n")


def select_users_where_email_start_b(cursor):
    print(f"Select emails")
    print("_____________________________________________________________________\n")

    input_char = input("Enter b: ")
    print("_____________________________________________________________________\n")


    char_word = input_char+'%'

    select_query = """
        select email from users where email like %s
    """

    try:
        cursor.execute(select_query,(char_word,))

        emails = cursor.fetchall()

        for email in emails:
            print(email[0])
        print("_____________________________________________________________________\n")

    except Exception as e:
        print(f"Error select data from database: {e}")

    print(f"Users successfully selected")
    print("_____________________________________________________________________\n")


def get_user():

    select_users_where_email_start_b(cur)

    con.commit()

    con.close()

def write_user_to_db(cursor, list_users):

    insert_into_db_list_users(cursor, list_users)

    con.commit()

    con.close()
