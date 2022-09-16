'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요시간은 5~50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요시간 5~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''
# 승객을 받을 소요시간을 입력받는다.
# 승객별 운행 소요시간은 2~60분 사이의 난수로 정해진다.
from random import *
passenger=[]
cnt = 0
while 1:
    try:
        start,end=map(int,input('매칭할 소요시간을 공백을 두고 입력해주세요(예. 1 30) : ').split())
        break
    except Exception as e:
        print('다시 입력해주세요')
        continue
for i in range(1,51):
    time = randint(2,60)
    yesNo = ' '
    if time >= start and time <= end:
        yesNo = 'O'
        cnt += 1
    passenger.append([i,time,yesNo]) # [[손님 번호, 소요시간, 탑승여부],[손님번호, 소요시간, 탑승여부]...]
for i in range(50):
    print("[%s] %d번째 손님 (소요시간 : %d분)"%(passenger[i][2],passenger[i][0],passenger[i][1]))
print('총 탑승 승객 : %d분'%cnt)