# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Customer:
    def __init__(self, name, account_no, account_type, balance):
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance

    def deposit(self):
        amount = float(input('enter the amount to be deposited:'))
        self.balance += amount
        print('Amount Deposited: ', amount)
        print('\nNew Balance: ', self.balance)

    def withdraw(self):
        amount = float(input('enter the amount to be withdrawn:'))
        if self.balance >= amount:
            self.balance -= amount
            print('Amount withdrawn: ', amount)
        else:
            print('Not enough balance')
        print('\nNew Balance: ', self.balance)

    def account(self):
        print('\nCustomer Name: ', self.name)
        print('\nAccount number: ',self.account_no)
        print('\ntype: ',self.account_type)
        print('\nNet Balance', self.balance)


customer = Customer('Ram Krishna','6105434278','savings',100000)
customer.deposit()
customer.withdraw()
customer.account()
