class Car:
    def __init__(self,speed):
        self.speed = speed

    def setSpeed(self,speed):
        self.speed = speed
    def getDesc(self):
        return '차량 = ({})'.format(str(self.speed))

class SportsCar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo = turbo

    def setTurbo(self,turbo):
        self.turbo = turbo

print('(1)----Car 클래스 상속에 의한 SportsCar 클래스 생성')
obj = SportsCar(100,True)
print(obj.getDesc())
obj.setTurbo(False)
