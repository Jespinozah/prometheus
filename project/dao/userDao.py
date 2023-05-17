from project.models.user import User
from typing import List

from project.database import db

class UserDao:
    @staticmethod
    def get_users() -> List[User]:
        return db.session.query(User).all()

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return (
            db.session.query(User).filter_by(username = username).first()
        )
