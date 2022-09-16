'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석율을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 :  [2,3,4]
-- 축하합니다 --
'''
# 조건1 : 당첨자 범위를 입력받아서 뽑는다
# 조건2 : 치킨 당첨자 2명으로 늘린다
from random import *
commentID = []
start,ends = 0,5 # 시작번호, 끝번호
while True:
    try:
        start,ends = map(int, input('시작할 숫자와 끝 숫자를 공백으로 구분하여 입력해주세요 (최소 5개 차이나도록) : ').split())
        if abs(start-ends)<4:continue # 5명을 뽑을 수 있는지 판단
        break
    except Exception as e:
        print('잘못 입력하셨습니다.') # 숫자가 아닌 다른 것을 입력 했을때
        continue
if start > ends: start, ends = ends, start # 숫자 대소 관계에 따라 range 오류 없애 주기 위함
for i in range(start,ends+1):
    commentID.append(i)
shuffle(commentID)
winner = sample(commentID,5)
print('-- 당첨자 발표 --\n치킨 당첨자 : ' + str(winner[:2]) +'\n커피 당첨자 : ', winner[2:], '\n-- 축하합니다 --')