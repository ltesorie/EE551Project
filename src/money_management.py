# this function allows existing users to log in
def login(userinput, userpassword):

    def password_check(userpassword):
        attempts = 3
        while attempts > 0:
            if userpassword in passwords:
                return True
            else:
                attempts -= 1
                userpassword = input("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")

        print("User Account is not available at this time please try again later, Thank you.")
        exit()
    usernames, passwords, balances = user_files()
    if userinput in usernames:
        password_check(userpassword)
        print("User Menu")
    else:
        choice = input("""User not found
        Press 1 to Restart
        Press 2 to Create New User
        Press 3 to Exit
        """)
        if choice == 1:
            userinput = input("Welcome! Please Enter your Username: \n")
            userpassword = input("Please enter your 4 digit pin code: \n")
            login(userinput, userpassword)
        elif choice == 2:
            print("make new user function")
        else:
            exit()

# This function reads all stored user information and parses the files to store into lists
def user_files():
    usernames = []
    passwords = []
    balances = []

    with open("User_Names.txt", 'r') as usernamefile:
        for line in usernamefile:
            usernames.append(line[:-1])
    with open("Passwords.txt", 'r') as passfile:
        for line in passfile:
            passwords.append(line[:-1])
    with open("Balance.txt", 'r') as balancefile:
        for line in balancefile:
            balances.append(line[:-1])

    return usernames, passwords, balances

#class BankingActions(object):
#    def user_functions(self):


