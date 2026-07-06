# day 51
# returning to cyber security
class verification:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(self, input_password):
        is_valid = self.password == input_password
        if not is_valid:
            print("Incorrect password. Access denied.")
        return is_valid

    def verify_username(self, input_username):
        is_valid = self.username == input_username
        if not is_valid:
            print("Incorrect username. Access denied.")
        return is_valid
