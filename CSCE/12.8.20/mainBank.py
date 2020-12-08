class BankAccount():
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance
    def Check(self, user):
        if(user == self.accountnumber):
            print("The Balance is: $" + str(self.balance))
        else:
            print("Wrong Number")

testAccount = BankAccount(1234, 12345)
BankAccount.Check(testAccount, 123)
BankAccount.Check(testAccount, 1234)