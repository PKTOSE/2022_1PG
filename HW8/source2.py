# 리스트에서 두번째로 큰 요소 찾기
numList = [10,20,4,45,99] # 기본 리스트

print('==========(1)==========') # for, if 이용
list1 = numList

def sortNum(list1): # 정렬 함수
    for i in range(len(list1)):
        if list1[i] == list1[-1]: return list1
        if list1[i] > list1[i+1]: list1[i],list1[i+1] = list1[i+1],list1[i];sortNum(list1)

list1 = sortNum(list1)
print(f"Second Max Element is {list1[-2]}")

print('==========(2)==========') # sort 이용
list2 = numList
list2.sort();list2.reverse()
print(f'Second Max Element is {list2[1]}')

print('==========(3)==========') # remove 이용
list3 = numList
newList = set(list3)
newList.remove(max(newList))
print(f'Second Max Element is {max(newList)}')