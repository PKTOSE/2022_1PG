# 소수 찾기

def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def primeNumber(x,y):
    for i in range(x,y+1):
        if isPrime(i):
            return i
    return -1

a = int(input('소수인지 확인할 숫자를 입력하세요: '))
print(a,'는 소수인가? ',isPrime(a))
x,y = map(int,input('두수 사이의 첫 소수를 찾으려 합니다 :').split())
if x>y: x,y=y,x
if primeNumber(x,y) != -1:
    print('{},{} 사이의 첫 소수는 {}입니다.'.format(x,y,primeNumber(x,y)))
else:
    print('{},{} 사이에는 소수가 없습니다.'.format(x,y))