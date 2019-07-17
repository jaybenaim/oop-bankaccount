class BankAccount: 
    interst_rate = .01
    accounts = [] 

    def __init__(self): 
        self.balance = 0 
    # def __str__(self): 
    #     return f'{self.balance}'

    def deposit(self, amount): 
        self.balance += amount 

    def __repr__(self): 
        return f'{self.balance}'

    def withdraw(self, amount): 
        self.balance -= amount 
    @classmethod
    def create(cls): 
       # makes an instance of bank account 
        new_account = BankAccount() 
        cls.accounts.append(new_account) 
        return new_account 

    @classmethod 
    def total_funds(cls): 
        return sum(account.balance for account in cls.accounts)
        
    @classmethod 
    def interest_time(cls): 
        for account in cls.accounts:
            rate = account.balance * cls.interst_rate 
            account.balance += rate 

my_account = BankAccount.create()

# print(my_account) 

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0