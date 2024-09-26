import os
import uuid

import bcrypt
from faker import Faker

from user import User

fake = Faker()


def generate_users(num_users):
    list_of_users = []

    print(f"Generating {num_users} users")
    print("_____________________________________________________________________")
    for _ in range(num_users):
        user = User(
            id=fake.uuid4(),
            username=fake.user_name(),
            email=fake.email(),
            password=generate_pass(fake.password()),
        )
        list_of_users.append(user)

    return list_of_users

def generate_pass(password):

    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(bytes, salt)
