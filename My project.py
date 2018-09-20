# Basic code by adamdev12


# signin allows the user to sign in
def signin():
    # sign in function.
    print('log in')
    valid = False
    while not valid:
        username = input('Username: ')
        password = input('Password: ')

        # TODO: Replace with actual login code.
        if username == 'adam' and password == '0000':
            valid = True
        else:
            print('incorrect username/password')
    


# validate checks if the password is long enough.
def validate():
    while True:
        password = input('Enter a password: ')
        if len(password) < 7:
            print('password must be at least 7 characters')

        elif password.isdigit():
            print('password must be 7 characters or more')
        else:
            print('password is okay')
            break


# signup creates a new user account.
def signup():
    print('signup')
    print('sign up screen.')
    global user
    password = ''
    fname = input('First Name: ')
    fullname = input('Last Name: ')
    username = input('Username: ')
    validate()
    email = input('E-mail: ')
    dateofbirth = input('Date Of Birth: ')



print('OCR tunes!')
print('1) log in?')
print('2) sign up?')
choice = input('Please choose an option.')

while True:
    if choice == '1':
        # goto sign in
        user = signin()
        break
    elif choice == '2':
        # goto signup
        user = signup()
        break
    else:
        choice = input
        print('Please choose option 1 or 2')

# TODO: Do something after logging in.
print('Nothing to do, exiting...')
