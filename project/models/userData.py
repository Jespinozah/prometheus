from .user import User

class UserData:
    def __init__(self, user: User):
        if user is not None:
            self.first_name = user.first_name
            self.last_name = user.last_name
            self.email = user.email
            self.password = user.password
            self.username = user.username