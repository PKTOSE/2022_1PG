import time, random, timeit


# list generator
def createList():
    random.seed(a=None, version=2)
    list1 = list(i for i in range(10000))
    random.shuffle(list1)
    return list1

# selection sorting
def selectionSort(li:list):
    for i in range(len(li)):
        minIdx = i
        for j in range(i+1,len(li)):
            if li[minIdx] > li[j]:
                minIdx = j
        li[i], li[minIdx] = li[minIdx], li[i]

# Bubble
def bubbleSort(li:list):
    n = len(li)
    for i in range(n):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

# Insertion
def insertionSort(li:list):
    for i in range(1,len(li)):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

numList = createList()
# print(f'Original List: {numList}')

selectionTime1 = time.time()
selectionList = list(numList)
#print(f'Original list: {selectionList}')
selectionSort(selectionList)
selectionTime2 = time.time(); selectionTime = selectionTime2 - selectionTime1
#print(f'Sorted list by Selection Sort: {selectionList}')

bubbleTime1 = time.time()
bubbleList = list(numList)
#print(f'Original list: {bubbleList}')
bubbleSort(bubbleList)
bubbleTime2 = time.time(); bubbleTime = bubbleTime2 - bubbleTime1
#print(f'Sorted list by Bubble Sort: {bubbleList}')

insertionTime1 = time.time()
insertionList = list(numList)
#print(f'Original list: {insertionList}')
insertionSort(insertionList)
insertionTime2 = time.time(); insertionTime = insertionTime2 - insertionTime1
#print(f'Sorted list by Insertion Sort: {insertionList}')

basicTime1 = time.time()
basicList = list(numList)
basicList.sort()
basicTime = time.time() - basicTime1



print(f"Time for Selection Sorting: {selectionTime} s")
print(f'Time for Bubble Sorting: {bubbleTime} s')
print(f'Time for Insertion Sorting: {insertionTime} s')
print('Time for Sorting Function: %f s'%basicTime)