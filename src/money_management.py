

# This class log in contains and accesses the information from users and stores it
# This class also can find or create any user
class LogIn(object):
    # this function allows existing users to log in
    def existing_user(self, userinput, userpassword):
        def password_check(password):
            attempts = 3
            while attempts > 0:
                if password in passwords:
                    return True
                else:
                    attempts -= 1
                    password = input("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")

            print("User Account is not available at this time please try again later, Thank you.")
            exit()
        usernames, passwords, balances = self.user_files()
        if userinput in usernames:
            password_check(userpassword)
            a = BankActions(userinput, userpassword)
            a.user_menu()
        else:
            choice = input("""User not found
            Press 1 to Restart
            Press 2 to Create New User
            Press 3 to Exit
            """)
            if choice == 1:
                userinput = input("Welcome! Please Enter your Username: \n")
                userpassword = input("Please enter your 4 digit pin code: \n")
                self.existing_user(userinput, userpassword)
            elif choice == 2:
                print("make new user function")
            else:
                exit()

    # This function reads all stored user information and parses the files to store into lists
    def user_files(self):
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

    def new_user(self, desired_username):
        usernames, passwords, balances = self.user_files()
        if desired_username not in usernames:
            a = open("User_Names.txt", 'a')
            a.write(desired_username + '\n')
            a.close()
        else:
            new_name = input("Username is taken. Please choose something else: \n")
            self.new_user(new_name)
        def create_password():
            new_password = input("Please choose a pin number of at least 4 digits: \n")
            if len(new_password) < 4:
                create_password()
            else:
                a = open("Passwords.txt", 'a')
                a.write(new_password + '\n')
                a.close()
                passcode = new_password
                self.existing_user(desired_username, passcode)
        balance = input("What is your starting account balance? \n")
        ask = open("Balance.txt", 'a')
        ask.write(balance + '\n')
        ask.close()
        create_password()
        "User Created: You will be redirected to log in using credentials \n"


# This will perform all bank actions for the simulation, providing withdrawal, deposit, and balance information
# Within this class there are multiple functions that are utilized by the program
class BankActions(object):
    def __init__(self, userinput, userpassword):
        self.username = userinput
        self.password = userpassword

    def expense(self):
        print("$$$")

    def income(self):
        print("$$$")

    def accountbalance(self):
        print("$$$")

    def user_menu(self):
        print("""~~~Budget App Mobile~~~ \n\t-- Account Menu Options --""")
        user_choice = int(input("""
        1. Log & Check Expense
        2. Log & Check Income
        3. Check Account Balance
        4. Exit 
        Enter Corresponding Number for Choice: \n"""))

        if user_choice == 1:
            self.expense()
        elif user_choice == 2:
            self.income()
        elif user_choice == 3:
            self.accountbalance()
        else:
            exit()
