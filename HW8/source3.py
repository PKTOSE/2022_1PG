# 숫자 리스트에서 짝수 홀수 세기

numList = [10,21,4,45,66,93,11]

print('=====(1)=====') # for loop
evenCnt,oddCnt = 0,0
for i in numList:
    if i%2 == 0:
        evenCnt += 1
    else: oddCnt += 1
print(f'Even numbers in list : {evenCnt}')
print(f'Odd numbers in list : {oddCnt}')

print('=====(2)=====') # while loop
evenCnt,oddCnt = 0,0; num = 0
while num<len(numList):
    if numList[num]%2 == 0: evenCnt += 1
    else : oddCnt += 1
    num += 1
print(f'Even numbers in list : {evenCnt}')
print(f'Odd numbers in list : {oddCnt}')

print('=====(3)=====') # list comprehension
oddCnt = [num for num in numList if num%2 != 0]
evenCnt = len(numList) - len(oddCnt)
print(f'Even numbers in list : {evenCnt}')
print(f'Odd numbers in list : {len(oddCnt)}')