import json


class Case1(object):
    # this function initializes a registered user and checks their credentials in the system, by comparing to the json
    # file
    def __init__(self):
        user_input = 'ltesorie'
        with open('test_json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if user_input.upper() in user['username'].upper():
                    print("found username")
                    self.username = user['username'].upper()
                    self.password = user['password']
                    self.balance = user['balance']
                    self.transactions = user['transactions']
                    self.check_password()
                    break
                elif user_input.upper() not in user['username'].upper():
                    print("...")
                print("Sorry could not locate the username " + user_input + ' please try again or create a new account')

    # This function takes in a user's password and checks it against the key on file
    # the user has 3 tries to access their information otherwise it will return to the main menu
    def check_password(self):
        user_input = '1108'
        attempts = 3
        while attempts > 1:
            if user_input == self.password:
                print("Case 1: Correct Username & Correct Password")
                break
            else:
                attempts -= 1
                user_input = input("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")
            print("User Account is not available at this time please try again later, Thank you.")

class Case2(object):
    # this function initializes a registered user and checks their credentials in the system, by comparing to the json
    # file
    def __init__(self):
        user_input = 'ltesorie'
        with open('test_json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if user_input.upper() in user['username'].upper():
                    print("found username")
                    self.username = user['username'].upper()
                    self.password = user['password']
                    self.balance = user['balance']
                    self.transactions = user['transactions']
                    self.check_password()
                    break
                elif user_input.upper() not in user['username'].upper():
                    print("...")
                print("Sorry could not locate the username " + user_input + ' please try again or create a new account')

    # This function takes in a user's password and checks it against the key on file
    # the user has 3 tries to access their information otherwise it will return to the main menu
    def check_password(self):
        attempts = 3
        count = 0
        user_input = '1234'
        while attempts > 1:
            if user_input == self.password:
                print("Case 1: Correct Username & Correct Password")
                break
            else:
                nums = ['5678', '9101', '8008']
                if count < 3:
                    user_input = nums[count]
                    count += 1
                attempts -= 1
                print("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")
        print("Case II Error: User Account is not available at this time please try again later, Thank you.")

class Case3(object):
    # this function initializes a registered user and checks their credentials in the system, by comparing to the json
    # file
    def __init__(self):
        user_input = 'fakeuser'
        with open('test_json.txt') as outfile:
            data = json.load(outfile)
            for user in data['users']:
                if user_input.upper() in user['username'].upper():
                    print("found username")
                    self.username = user['username'].upper()
                    self.password = user['password']
                    self.balance = user['balance']
                    self.transactions = user['transactions']
                    self.check_password()
                    break
                elif user_input.upper() not in user['username'].upper():
                    print("...")
            print(" Case III: Sorry could not locate the username " + user_input + ' please try again or create a new account')

    # This function takes in a user's password and checks it against the key on file
    # the user has 3 tries to access their information otherwise it will return to the main menu
    def check_password(self):
        user_input = '1124'
        attempts = 3
        while attempts > 1:
            if user_input == self.password:
                print("Case 1: Correct Username & Correct Password")
                break
            else:
                attempts -= 1
                user_input = input("Incorrect Code." + str(attempts) + " attempts remaining \nplease try again: \n")
            print("User Account is not available at this time please try again later, Thank you.")

# Sets up correct username and correct password scenario
Case1()
# Sets up correct username, but incorrect password scenario
Case2()
# Sets up incorrect/not used username scenario
Case3()
