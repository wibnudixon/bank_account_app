class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self, path):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self,filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee
    
    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("balance.txt",1)
checking.transfer(10)
print(checking.balance)
checking.commit("balance.txt")

# account=Account("balance.txt")
# print(account.balance)
# account.deposit(10)
# account.withdraw(100)
# print(account.balance)
# account.commit("balance.txt")

