# selection sorting

def selectionSort(li:list):
    for i in range(len(li)):
        minIdx = i
        for j in range(i+1,len(li)):
            if li[minIdx] > li[j]:
                minIdx = j
        li[i], li[minIdx] = li[minIdx], li[i]

numList = [64, 25, 12, 22, 11]
print('Original List: {}'.format(numList))
selectionSort(numList)
print('Sorted list by Selection Sort: {}'.format(numList))
