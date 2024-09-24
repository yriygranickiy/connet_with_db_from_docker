from faker import Faker

from user import User

fake = Faker()


def generate_users(num_users):
    list_of_users = []
    for _ in range(num_users):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        list_of_users.append(user)

    return list_of_users
