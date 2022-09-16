'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함.
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함.
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외함.

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.
'''

# 문제 수정
# 조건 a : 매월 3~5일은 스터디 준비를 위해 제외
# 조건 b : 매월 2회 온라인 / 2회 오프라인 -> 오프라인 2회의 날짜 뽑기(단, 두 날짜간 간격  최소 5일)

from random import *
def sortDate(dateList):
    if dateList[0] < dateList[1]:
        return dateList
    else:
        dateList[0], dateList[1] = dateList[1], dateList[0]
        return dateList
date = []
cnt = 0
while True:
    meetingDate = randint(1,28)
    if meetingDate in range(3,6):
        continue
    elif len(date) != 0:
        if abs(meetingDate - date[0]) > 5:
            date.append(meetingDate)
            break
        else:
            continue
    else:
        date.append(meetingDate)
        cnt += 1

date = sortDate(date)
print('오프라인 스터디 모임 날짜는 매월 %d, %d일로 선정되었습니다.'%(date[0],date[1]))