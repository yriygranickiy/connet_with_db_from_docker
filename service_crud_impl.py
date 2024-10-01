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

def insert_into_db_user(cursor,user):
    insert_query ="""
        Insert into users (id,username, email, password)
        values (%s, %s, %s, %s)
    """

    try:
        cursor.execute(insert_query, (user.id, user.username, user.email, user.password))
    except Exception as e:
        print(f"Error added data in database: {e}")

    print("users successfully added")
    print("_____________________________________________________________________\n")

def select_all_users(cursor):
    print(f"Select all users")
    print("_____________________________________________________________________\n")

    select_query = """
        select username,email from users
    """
    try:
        cursor.execute(select_query)

        users = cursor.fetchall()

        for user in users:
            print(user)
        print("_____________________________________________________________________\n")
    except Exception as e:
        print(f"Error selected data in database: {e}")
    print(f"Users successfully selected")
    print("_____________________________________________________________________\n")

def select_users_where_email_start__any_symbols(cursor):
    print(f"Select emails")
    print("_____________________________________________________________________\n")

    input_char = input("Enter b: ")
    print("_____________________________________________________________________\n")


    char_word = input_char+'%'

    select_query = """
        select username,email from users where email like %s
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


def delete_user_by_username(cursor, user_name):

    delete_query = """
        delete from users where username like %s
    """

    try:

        cursor.execute(delete_query, (user_name,))

        print("User successfully deleted")
        print("_____________________________________________________________________\n")
    except Exception as e:
        print(f"Error deleting data in database: {e}")

def update_user_email_by_username(cursor, user_name, new_email):
    update_query = """
        update users set email = %s where username=%s
    """

    try:

        cursor.execute(update_query, (new_email, user_name))

        print("User successfully updated")
        print("_____________________________________________________________________\n")
    except Exception as e:
        print(f"Error updating data in database: {e}")


