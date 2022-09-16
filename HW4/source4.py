'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전제 5억 2007년
송파 빌라 월세 500/50 2000년
'''
# 평수 추가
# 집을 추가할 수 있게 한다. -1을 입력하면 입력이 종료되게 한다.
class House:
    # 매물 초기화
    def __init__(self,location,house_type,square_metres,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.square_metres = square_metres
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # 매물 정보 표시
    def show_deail(self):
        print('{} {} {} {} {} {}'.format(self.location,self.house_type,self.square_metres,self.deal_type,self.price,self.completion_year))

houseINFO = [['강남','아파트','7평','매매','10억','2010년'],['마포','오피스텔','5평','전세','5억','2007년'],['송파','빌라','4평','월세','500/50','2000년']]

while 1:
    plusNew = int(input('집을 추가하시겠습니까? (-1 이면 입력 종료 / 그 외의 숫자는 입력 진행) :'))
    if plusNew == -1:break
    try:
        a = [*map(str, input('지역 형태 평수 거래방법 가격 준공년도 : ').split())]
        if len(a) != 6: raise Exception('잘못입력하였습니다.^^')
        houseINFO.append(a)
    except Exception as e:
        print(e,'\n잘못입력하여 집 입력을 종료합니다.')
        break

print('총 {}대의 매물이 있습니다.'.format(len(houseINFO)))
for i in range(len(houseINFO)):
    maemool = House(*houseINFO[i])
    maemool.show_deail()