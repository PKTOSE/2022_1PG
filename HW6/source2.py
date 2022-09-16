# 최대 공약수 찾기

def gcd(x,y):
    r = x%y
    x,y = y,r
    if y == 0:
        return x
    return gcd(x,y)

def gcd1(x,y):
    gcd=1
    for i in range(2,y+1):
        if x%i == 0 and y%i == 0:
            gcd = i
    return gcd

print('두 수 사이의 최대 공약수를 찾으려 합니다.')
x,y = map(int,input('두 수를 입력하세요 : ').split())
if x<y: x,y=y,x
print('{}, {} 사이의 최대공약수(by 유클리드 방법) = {}'.format(x,y,gcd(x,y)))
print('{}, {} 사이의 최대공약수(by 일반 반복 방법) = {}'.format(x,y,gcd1(x,y)))