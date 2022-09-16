# Insertion

def insertionSort(li:list):
    for i in range(1,len(li)):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

numlist = [12, 11, 5, 13, 6]
print('Original list: {}'.format(numlist))
insertionSort(numlist)
print('Sorted list by Insertion Sort: {}'.format(numlist))