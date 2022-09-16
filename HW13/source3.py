class BankAccount:
    def __init__(self,name,number,balance):
        self.balance = balance
        self.name = name
        self.number = number

    def withDraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self,name,number,balance,interestRate):
        super().__init__(name,number,balance)
        self.interestRate = interestRate

    def setInterestRate(self,interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate

    def addInterest(self):
        self.balance += self.balance*self.interestRate

class CheckAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withDrawCharge = 10000

    def withDraw(self, amount):
        return BankAccount.withDraw(self, amount + self.withDrawCharge)

print('(1)----------은행계좌 클래스 및 클래스 상속----------')
a1 = SavingAccount('홍길동', 123456, 10000, 0.05)
a1.addInterest()
print('저축 예금의 잔액 = {}'.format(a1.balance))

a2 = CheckAccount('김철수', 1234567, 2000000)
a2.withDraw(100000)
print('당좌 예금의 잔액 = {}'.format(a2.balance))