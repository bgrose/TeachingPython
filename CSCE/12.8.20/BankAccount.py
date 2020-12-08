class BankAccount():
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance
    def Check(self):
        user = int(input('Enter the Account Number: '))
        if(user == self.accountnumber):
            print("The Balance is: $" + str(self.balance))
        else:
            print("Wrong Number")
