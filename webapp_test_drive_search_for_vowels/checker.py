from flask import session

from functools import wraps


def check_logged_in(func: object) -> object:
    """Decorator to check whether user is logged in"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
