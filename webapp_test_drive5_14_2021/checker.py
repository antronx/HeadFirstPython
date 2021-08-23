from flask import session

from functools import wraps


"""Decorator to check wether user is logged in"""
def check_logged_in(func: object) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
