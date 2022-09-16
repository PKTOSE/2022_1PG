# Bubble

def bubbleSort(li:list):
    n = len(li)
    for i in range(n):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

numlist = [64, 34, 25, 12, 22, 11, 90]
print('Original List: {}'.format(numlist))
bubbleSort(numlist)
print('Sorted list by Bubble Sort: {}'.format(numlist))