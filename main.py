import utils


def main():
    users = utils.generate_users(25)

    for user in users:
        print(user)



if __name__ == "__main__":
    main()
