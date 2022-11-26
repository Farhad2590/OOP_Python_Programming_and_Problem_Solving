class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.minimum_withdraw = 100
        self.maximum_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount < self.minimum_withdraw:
            return f'No money for you. Mimimum Withdraw:{self.minimum_withdraw}'
        elif amount > self.maximum_withdraw:
            return f'You Crossed Daily Withdraw Limit: {self.maximum_withdraw}'
        elif amount >self.balance:
            return 'You are broke !!! No money for you'
        else:
            self.balance = self.balance - amount
            return f'Here Is Your Money: {amount}'
    def deposit(self,amount):
        self.balance = self.balance + amount

My_bank = Bank(8000)
reply = My_bank.withdraw(1000)
print(reply)
print(My_bank.get_balance())
My_bank.deposit(5000)
print(My_bank.get_balance())