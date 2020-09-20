# Imports
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from typing import List, Optional
# Custom Libraries
from data import db_session
from data.account.users import User


def find_user_by_email(email: str) -> List[User]:
    session = db_session.create_session()

    return session.query(User).filter(User.email == email).first()


def find_user_by_username(username: str) -> List[User]:
    session = db_session.create_session()

    return session.query(User).filter(User.username == username).first()


def find_user_by_id(id: int) -> List[User]:
    session = db_session.create_session()

    uid = session.query(User).filter(User.id == id).first()
    session.close()

    return uid


def create_user(name: str, username: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    if find_user_by_username(username):
        return None

    user = User()
    user.name = name
    user.username = username
    user.email = email
    user.hashed_password = hash_text(password)

    session = db_session.create_session()
    session.add(user)
    session.commit()
    session.close()

    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=174500)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(username: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    user = session.query(User).filter(User.username == username).first()
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user
