#Basic code by adamdev12

def signin():
    #sign in function.
    print("log in")
    valid = False
    while valid == False:
        username = input("username: ")
        password = input("password: ")
        if username == "adam" and password == "0000":
            valid = True
        else:

            print('incorrect username/password')

def validate():
    while True:
        password = input =('Enter a password: ')
        if len(password) < 7:
            print('password must be at least 7 characters')

        elif password.isdidget():
            print('password must be 7 characters or more')
        else:
            print('password is okay')
            break
                           
def signup():

    #signup function

    print("signup")

    print('sign up screen.')

    global user

    global password

    password = ""

    user = []

    fname = input('enter your name: ')

    username = input('enter a username: ')

    validate()

    email = input("E-mail: ")

    fullname = input("Full Name: ")

    dateofbirth = input("Date Of Birth: ")

    user.append(username)

    user.append(password)

    user.append(email)

    user.append(fullname)

    user.append(dateofbirth)



print("OCR tunes!")

print("1) log in?")

print("2) sign up?")

choice = input('Please choose an option.')




validchoice = False

while validchoice == False:

    if choice == "1" :

        #goto sign in

        signin()

        validchoice = True

    elif choice == "2" :

    



        #goto signup

        signup()

        validchoice = True

    else:

        choice = input

        ("please choose option 1 or 2")







def list10():

    print('last 10 songs listened to')

    global movielist

    movielist = []

    load()

    length = len(movielist)

    i = 0

    found = False

    while found == False and i < length :

            #OUTPUT THE PRODUCT IF FOUND.

            if userlist[i][0] == username:

                n = 9

                for n in range (9,19):

                    movielist.append(userlist[i][n])

                found = True

            i = i + i

    printlist(i)





