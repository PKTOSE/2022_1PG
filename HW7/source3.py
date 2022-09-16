# 구구단 출력하기
def gugudan(n):
    for i in range(n,10):
        for j in range(1,10):
            print('%d X %d = %d'%(i,j,i*j))
    return
print('n단부터 9단까지 구구단을 출력합니다.')
n = int(input('몇단부터 출력하시겠습니까? : '))
gugudan(n)
print('='*10)

# 피타고라스 삼각형의 세 변의 경우의 수 찾기
def findPythNum(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i**2 + j**2 == k**2:
                    print('{} {} {}'.format(i,j,k))
    return
print('피타고라스 삼각형을 이루는 세변의 경우 찾기')
n = int(input('변의 길이의 최대값을 입력하세요: '))
findPythNum(n)
print('='*10)

# 윤년 판별하기
def checkLeapYear(year:int):
    if (year%4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('%d년은 윤년입니다.'%year)
    else:
        print('%d년은 윤년이 아닙니다.')
print('윤년 판별하기')
year = int(input('년도를 입력하세요: '))
checkLeapYear(year)
