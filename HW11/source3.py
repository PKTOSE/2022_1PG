# 클래스 기반의 은행계좌 & 자동차
class BanKAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self,amount):
        self.__balance -= amount
        print('통장에서 {}원이 출금되었습니다.'.format(amount))
        return self.__balance

    def deposit(self,amount):
        self.__balance += amount
        print('통장에 {}원이 입금되었습니다.'.format(amount))
        return self.__balance

print('1)==========')
a = BanKAccount()
a.deposit(100)
a.withdraw(10)

class Car:
    def __init__(self,spd = 0, gear = 1, colour = 'white'):
        self.spd = spd
        self.gear = gear
        self.colour = colour

    def setSpeed(self,spd):
        self.spd = spd

    def setGear(self,gear):
        self.gear = gear

    def setColour(self,colour):
        self.colour = colour

    def __str__(self):
        return '({}, {}, {})'.format(self.spd,self.gear,self.colour)\

print('2)==========')
myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
print(myCar)