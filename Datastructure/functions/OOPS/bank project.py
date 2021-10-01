

class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance += amount    

    def withdraw(self,amount):
        if self.balance-amount  >= self.min_balance:
            self.balance -= amount
        else:
            print("sorry not enough funds!")      

    def statement(self):
        print("Account Balance: ₹{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account : Balance ₹{}".format(self.name,self.balance)


x=Current("Yogesh",500)
x.deposit(300)
print(x.statement())

x.withdraw(1000)
print(x.statement())

x.withdraw(800)
print(x.statement())

print(x)

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Saving Account : Balance ₹{}".format(self.name,self.balance)
    




         

