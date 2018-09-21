#!/usr/bin/env python3
# Basic code by adamdev12


# Login code
import login
# custom errors
import error


print('OCR tunes!')
print('[1] log in?')
print('[2] sign up?')
choice = input('Please choose an option: ')


while True:
    if choice == '1':
        # Signing in.
        try:
            # Try logging in
            username, mail = login.verify_user()
            print("Signed in successfully.")
            break

        except error.PasswordIncorrect:
            # If the password is incorrect, not login
            print("Password wrong.")

        except error.UserNotFound:
            # If the user is not registered, not login
            print("Username not found.")

    elif choice == '2':
        # Sign up.

        # Create a new user account
        print("Creating a new user account:")
        login.create_user()

        # Let the user login with that user account.
        print("Now log in with your new account:")
        try:
            # Try logging in
            username, mail = login.verify_user()
            print("Signed in successfully.")
            break

        except error.PasswordIncorrect:
            # If the password is incorrect, not login
            print("Password wrong.")

        except error.UserNotFound:
            # If the user is not registered, not login
            print("Username not found.")

    else:
        # User did not type 1 or 2
        print('Please choose option [1] or [2].')

# TODO: Do something after logging in.
print('Hello {}, your mail was {}'.format(username, mail))



