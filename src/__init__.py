from money_management import *

# This Function Stars up the GUI for person to interact with
def main():
    print("~~~Budget App Mobile~~~ \n\t-- Main Menu --")
    user_choice = int(input("""
    1. Existing User
    2. New User
    3. Exit Application
    Enter Corresponding Number for Choice: """))

    if user_choice == 1:
        userinput = input("Welcome! Please Enter your Username: \n")
        userpassword = input("Please enter your 4 digit pin code: \n")
        login(userinput, userpassword)
    elif user_choice == 2:
        print(2)
    else:
        exit()


main()
