import utils


class User():
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"id : {self.id},Username: {self.username}, Email: {self.email}, Password: {self.password}"


