import json
import os


# This class log in contains and accesses the information from users and stores it
# This class also can find or create any user
class LogInUser(object):
    def __init__(self):
        user_input = input("Welcome! Please Enter your Username: \n")
        with open('json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if user_input.upper() in user['username'].upper():
                    print("found username")
                    self.username = user['username'].upper()
                    self.password = user['password']
                    self.balance = user['balance']
                    self.transactions = user['transactions']
                    self.check_password()
                elif user_input.upper() not in user['username'].upper():
                    print("...")
        print("Sorry could not locate the username " + user_input + ' please try again or create a new account')

    def check_password(self):
        user_input = input("Welcome! Please Enter your Pincode: \n")
        attempts = 3
        while attempts > 1:
            if user_input == self.password:
                startup = BankActions(self.username, self.password, self.balance, self.transactions)
                startup.user_menu()
                return True
            else:
                attempts -= 1
                user_input = input("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")
        print("User Account is not available at this time please try again later, Thank you.")


class LogInNewUser(object):

    def add_json_obj(self, input_user):
        with open('json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if input_user.upper() != user['username'].upper():
                    approved_password, balance = self.create_password()
                    print(approved_password, balance)
                    self.append_json(input_user, approved_password, balance)
                    break
                else:
                    print('User Exists')
                    exit()
        print("restart and log in with information \n")

    def append_json(self, user, passcode, balance):
        entry = {
            "username": user,
            "password": passcode,
            "balance": balance,
            "transaction": balance
        }
        with open('json.txt', 'ab+') as f:
            f.seek(0, 2)
            if f.tell() == 0:
                f.write(json.dumps([entry]).encode())
            else:
                f.seek(-2, os.SEEK_END)
                f.truncate()
                f.write(' , '.encode())
                f.write(json.dumps(entry).encode())
                f.write(']'.encode())
                f.write('}'.encode())

    def create_password(self):
        password = input("Welcome! Please Enter your desired pincode: \n")
        if len(password) < 4 and password.isdigit() is True:
            print("Please have at least 4 digits and only numbers")
            self.create_password()
        else:
            balance = input("Welcome! Please Enter your starting balance: \n")
            return password, balance


class BankActions(object):
    def __init__(self, userinput, userpassword, userbalance, usertrans):
        self.username = userinput
        self.password = userpassword
        self.balance = userbalance
        self.transactions = usertrans

    def expense(self):
        transaction = input("Enter an expense number: \n")
        with open('json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if self.username.upper() in user['username'].upper():
                    entry = {
                        "transaction": [self.transactions, "-" + transaction]
                    }
                    with open('json.txt', 'ab+') as f:
                        f.(user['username'][self.username])
                        if f.tell() == 0:
                            f.write(json.dumps([entry]).encode())
                        else:
                            f.seek(-2, os.SEEK_END)
                            f.truncate()
                            f.write(' , '.encode())
                            f.write(json.dumps(entry).encode())
                            f.write(']'.encode())
                            f.write('}'.encode())


    def income(self):
        print("$$$")

    def account_balance(self):
        response = input("Your current account balance is: \n\t$" + self.balance + "\nWould you like to make another "
                                                                                   "transaction? (y/n): \n")
        if response.upper() == "Y":
            return True
        else:
            exit()

    def account_transactions(self):
        response = input("Account Transactions: \n\t$" + self.transactions + "\nWould you like to make another "
                                                                             "transaction? (y/n): \n")
        if response.upper() == "Y":
            return True
        else:
            exit()

    def user_menu(self):
        while True:
            print("""~~~Budget App Mobile~~~ \n\t-- Account Menu Options --""")
            user_choice = int(input("""
            1. Log & Check Expense
            2. Log & Check Income
            3. Check Account Balance
            4. List Account Transactions
            5. Exit 
            Enter Corresponding Number for Choice: \n"""))

            if user_choice == 1:
                self.expense()
            elif user_choice == 2:
                self.income()
            elif user_choice == 3:
                self.account_balance()
            elif user_choice == 4:
                self.account_transactions()
            else:
                exit()
