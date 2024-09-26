import test_connection
import utils


def main():

    users = utils.generate_users(25)

    for user in users:
        print(user)

    test_connection.test_connection(users)


if __name__ == "__main__":
    main()
