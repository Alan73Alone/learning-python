class BankAccount:
    def __init__(self,balance = 0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("余额不能为0")
        self._balance = value
        
    #存款
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self._balance += amount
        print(f"成功存款{amount}元，现余额为{self._balance}元")


    #取款
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        print(f"成功取款{amount}元，现余额为{self._balance}元")


    #获取余额信息
    def __str__(self):
        return f"BankAccount(余额={self._balance})"   