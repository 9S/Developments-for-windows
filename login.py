#!/usr/bin/env python3
# login.py
# A custom login system only using built-in libraries.


# storing user data
import json
# hashlib and uuid for hashing and salting of the password
import hashlib
import uuid
# secure input of the password
import getpass
# checking if file exists
import os

# import custom errors
import error


# loads the database from file
def load_database():
    # load database if exists
    if os.path.exists(database_location):
        # Open file and read the JSON data
        with open(database_location, 'r') as db:
            user_data = json.load(db)
    else:
        # otherwise just create an empty list to store the users
        # the file will be created on the save operation.
        user_data = []
    return user_data


# save_database writes the database to disk
def save_database():
    # Open file and write as JSON
    with open(database_location, 'w') as db:
        json.dump(user_data, db, sort_keys=True, indent=4)


# hash_password turns the password into a hash and salt.
def hash_password(prompt, salt=uuid.uuid4().hex):
    # Default value for salt is a random salt. This gives us the
    # option to send our own salt through this function

    #               Hashes the     password                             and the     salt
    password_hash = hashlib.sha512(getpass.getpass(prompt=prompt).encode('utf-8') + salt.encode('utf-8')).hexdigest()

    # return that hash and salt.
    return password_hash, salt


# create_user creates a new user and stores it in the database
def create_user():
    # Get username
    username = input('Username: ')
    # Instead of storing the password in a variable
    # just send it straight to the hashing function
    pw_hash, pw_salt = hash_password('Password: ')
    # get email address
    mail = input('E-Mail: ')

    # Put all that data into a dict
    user = {
        'username': username,
        'password_hash': pw_hash,
        'password_salt': pw_salt,
        'mail': mail
    }

    # add the user to the user list
    user_data.append(user)
    # save the data
    save_database()


# verify_user checks if the user exists and their password is right
def verify_user():
    # Get username
    username = input('Username: ')

    # Check if user exists
    for user in user_data:
        if user['username'] == username:
            pw_hash, _ = hash_password('Password: ', user['password_salt'])
            if pw_hash == user['password_hash']:
                return user['username'], user['mail']
            else:
                raise error.PasswordIncorrect

    raise error.UserNotFound(username)


# load database
database_location = 'users.json'
user_data = load_database()