from money_management import *


# This Function Stars up the GUI for person to interact with
# This Class is instantiated at the end of the program to start up the function
class StartUp(object):
    def __init__(self):
        print("~~~Budget App Mobile~~~ \n\t-- Main Menu --")
        user_choice = int(input("""
        1. Existing User
        2. New User
        3. Exit Application
        Enter Corresponding Number for Choice: """))

        if user_choice == 1:
            LogInUser()
        elif user_choice == 2:
            username = input("Welcome! Please Enter your Username: \n")
            start = LogInNewUser()
            start.add_json_obj(username)
        else:
            exit()


if __name__ == "__main__":
    StartUp()

