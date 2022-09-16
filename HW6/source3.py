# 거스름돈 계산하기
def calcChange(price,n1000,n500,n100):
    change=n1000*1000 +n500*500 +n100*100 - price
    money=[]
    money.append(str(change//500))
    change %= 500
    money.append(str(change//100))
    change %= 100
    money.append(str(change//50))
    change %= 50
    money.append(str(change//10))
    change %= 10
    money.append(str(change))

    return money

print('물건값과 지불금액을 입력하면 거스름돈 계산해줍니다.')
price = int(input('물건값을 입력해주세요 : '))
n1000,n500,n100 = map(int,input('1000원권, 500원, 100원 동전 수를 차례로 입력해주세요: ').split())
change = calcChange(price,n1000,n500,n100)
print('거스름돈 500원 : %s, 100원 : %s, 50원 : %s, 10원 : %s, 1원 : %s'%(change[0],change[1],change[2],change[3],change[4]))
