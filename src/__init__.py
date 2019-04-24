import money_management.py

# This Function Stars up the temp non-complicated GUI

def __init__():
    print("~~~Budget App Mobile~~~ \n\t-- Main Menu --")
    user_choice = int(input("""
    1. Existing User
    2. New User
    3. Exit Application
    
    Enter Corresponding Number for Choice: """))

    if user_choice == 1:
        print(1)
    elif user_choice == 2:
        Bank()
    else:
        exit()


__init__()
