import utils
from utils import add
print(utils.add(1,2))
print(add(3,4))

from bank import BankAccount
b = BankAccount(20)     #开户，初始余额为20
b.deposit(50)           #存款 50 -> 余额70  
b.withdraw(20)          #取款 20 -> 余额50
print(b)                #BankAccount(余额=50)

# property的用法:看起来想普通属性,实际走setter检查
b.balance = 100        #合法
print(b.balance)       #100
#b.balance = -5         #会抛valueError：余额不能为负数
