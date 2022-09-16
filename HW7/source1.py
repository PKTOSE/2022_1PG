#팩토리얼 계산하기
#1. for loop
def factorialFor(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
nFor = int(input('for문으로 펙토리얼을 계산할 숫자를 입력하세요 :'))
print('{}! -> for loop: {}'.format(nFor,factorialFor(nFor)))
#2. while loop
def factorialWhile(n):
    fact = 1
    i = 1
    while i<=n:
        fact *= i
        i += 1
    return fact
nWhile = int(input('while문으로 펙토리얼을 계산할 숫자를 입력하세요 :'))
print('{}! -> while loop: {}'.format(nWhile,factorialWhile(nWhile)))
#3. recursive
def factorialRecursive(n):
    if n == 1: return 1
    return n*factorialRecursive(n-1)

nRecur = int(input('재귀함수로 펙토리얼을 계산할 숫자를 입력하세요 :'))
print('{}! -> recursive: {}'.format(nRecur,factorialRecursive(nRecur)))