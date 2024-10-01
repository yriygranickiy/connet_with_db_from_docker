import uuid

import utils
from User import User
import service_crud


def menu():

    loop_programm = True

    while loop_programm:
        print("\n1. View all users")
        print("2. Add a user")
        print("3. Edit a user")
        print("4. Delete a user")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service_crud.get_all_users()

        elif choice == "2":
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            created_user = User(
                id=str(uuid.uuid4()),
                username=username,
                email=email,
                password= utils.generate_pass(password)
            )
            service_crud.create_user(created_user)

        elif choice == "3":
            username = input("Enter your username: ")
            email = input("Enter email u want: ")
            service_crud.update_user_email_by_username(username, email)

        elif choice == "4":

            username = input("Enter your username: ")
            service_crud.delete_user_by_username(username)

        elif choice == "5":
            loop_programm = False
        else:
            print("Invalid choice")
