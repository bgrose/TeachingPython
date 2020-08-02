#BankAccount class 
class Bankaccount: 
    def __init__(self, accountNum, baliInit):
        self.accountnumber = accountNum
        self.balance = baliInit
    def Check(self):
        Uinput = input("What is your account number?\n")
        if(Uinput == self.accountnumber):
            print("your Balance Is" + self.balance)
        else:
            print("Wrong Number")
        
s = Bankaccount(1111, 0)
s.Check()