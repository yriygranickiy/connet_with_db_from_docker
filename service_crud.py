import conection
import service_crud_impl

con = conection.connection_db()

cur = con.cursor()


def create_user(user):

    service_crud_impl.insert_into_db_user(cur, user)

    con.commit()

def get_user():

    service_crud_impl.select_users_where_email_start_b(cur)

    con.commit()


def get_all_users():

    service_crud_impl.select_all_users(cur)

    con.commit()


def delete_user_by_username(username):

    service_crud_impl.delete_user_by_username(cur, username)

    con.commit()

def write_users_to_db(list_users):

    service_crud_impl.insert_into_db_list_users(cur, list_users)

    con.commit()

def update_user_email_by_username(username, email):

    service_crud_impl.update_user_email_by_username(cur, username, email)

    con.commit()


