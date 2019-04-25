from money_management import *


# This Function Stars up the GUI for person to interact with
# This Class is instantiated at the end of the program to start up the function
class StartUp(object):
    def __init__(self):
        self.main()
        print("test feature")

    def main(self):
        print("~~~Budget App Mobile~~~ \n\t-- Main Menu --")
        user_choice = int(input("""
        1. Existing User
        2. New User
        3. Exit Application
        Enter Corresponding Number for Choice: """))

        if user_choice == 1:
            userinput = input("Welcome! Please Enter your Username: \n")
            userpassword = input("Please enter your 4 digit pin code: \n")
            start = LogIn()
            start.existing_user(userinput, userpassword)
        elif user_choice == 2:
            userinput = input("Welcome! Please Enter your desired Username: \n")
            start = LogIn()
            start.new_user(userinput)
        else:
            exit()


StartUp()

