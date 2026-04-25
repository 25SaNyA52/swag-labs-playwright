from utils.config import STANDARD_USER, LOCKED_USER, PASSWORD

VALID_USER = {
    "username": STANDARD_USER,
    "password": PASSWORD,
}

LOCKED_OUT_USER = {
    "username": LOCKED_USER,
    "password": PASSWORD,
}

INVALID_USER = {
    "username": "wrong_user",
    "password": "wrong_pass",
}
