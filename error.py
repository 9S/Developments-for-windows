#!/usr/bin/env python3
# error.py
# Contains all the custom errors needed throughout the program


# PasswordIncorrect is an error that gets raised when the
# entered password is incorrect
class PasswordIncorrect(Exception):
    pass


# UserNotFound is an error that gets raised when the user
# is not found in the database
class UserNotFound(Exception):
    def __init__(self, username):
        self.user = username
