
class User():

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password


    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Password: {self.password}, First name: {self.first_name}, Last name: {self.last_name}"
