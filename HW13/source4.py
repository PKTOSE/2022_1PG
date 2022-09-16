class Car:
    def __init__(self, speed, maker, model, colour, price):
        self.speed = speed
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price

    def setSpeed(self,speed):
        self.speed = speed
    def getDesc(self):
        return '차량 = ({})'.format(str(self.speed))
    def setMaker(self, maker):
        self.maker = maker
    def getMaker(self):
        return self.maker
    def getDesc(self):
        return '제조사: {}\n모델: {}\n색상: {}\n속도: {}\n가격: {}'.format(self.maker,self.model,self.colour,\
                                                                self.speed,self.price)

class SportsCar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo = turbo

    def setTurbo(self,turbo):
        self.turbo = turbo

class Truck(Car):
    def __init__(self,maker,model,colour,speed,price):
        super().__init__(speed,maker,model,colour,price)
        self.payload = 0

    def setPayload(self,payload):
        self.payload = payload
    def getPayload(self):
        return self.payload
    def getDesc(self):
        return '제조사: {}\n모델: {}\n색상: {}\n속도: {}\n가격: {}\n화물: {}'.format(self.maker,self.model,self.colour,\
                                                                self.speed,self.price,self.payload)

class Bus(Car):
    def __init__(self,maker,model,colour,speed,price):
        super().__init__(speed,maker,model,colour,price)
        self.num_of_seats = 0

    def set_num_of_seats(self,num):
        self.num_of_seats = num

    def get_num_of_seats(self):
        return self.num_of_seats
    def getDesc(self):
        return '제조사: {}\n모델: {}\n색상: {}\n속도: {}\n가격: {}'.format(self.maker,self.model,self.colour,\
                                                                self.speed,self.price,self.get_num_of_seats())



print('(1)----Car 클래스 상속에 의한 Truck 클래스 내 메소드 호출, 생성된 객체 정보 출력')
obj1 = Truck('BMW','520d','white',50,5000)
obj1.setPayload(1000)
print(obj1.getDesc())

print('(2)----Car 클래스 상속에 의한 Bus 클래스 내 메소드 호출, 생성된 객체 정보 출력')
obj2 = Bus('HUNDAI','bus','blue',60,4000)
obj2.set_num_of_seats(12)
print(obj2.getDesc())


