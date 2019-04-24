
class LogIn(object):
    def user_name(self, username, password):
        self.username = username
        self.password = password

    def checkusername(self, input_username):
        if input_username == self.username:
            input_password = input("Password: \n")
            if input_password == self.password:
                print("Welcome " + self.username + " !")
            else:
                print("Incorrect Password")
        else:
            print("User not found \n ")


class ClientProfile(LogIn):
    def __init__(self, total_income=0):
        self.totalincome = total_income


class Transaction(ClientProfile):
    def user_income(self):
        input_income = int(input('Total Income Received: '))
        self.totalincome += input_income
        return self.totalincome

    def user_expense(self):
        input_expense = int(input('Expense Amount: '))
        self.totalincome -= input_expense


# controls the accounts and storage of information
class Bank(object):
    def __init__(self):
        self.username
        self.password
        self.balance = filestore.customeraccount()


# manages balance of an account
class BankAccount(object):


# in charge of input, output, printing, and calling
class Interactive(object):
