# Merge Sort

def mergeSort(li:list):
    if len(li) > 1:
        mid = len(li) // 2
        L = li[:mid]
        R = li[mid:]

        mergeSort(L)
        mergeSort(R)

        li.clear()
        while len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                li.append(L[0])
                L.pop(0)
            else:
                li.append(R[0])
                R.pop(0)
        for i in L:
            li.append(i)
        for i in R:
            li.append(i)

li = [10, 7, 3, 9, 1, 5]
print("Original list: {}".format(li))
mergeSort(li)
print('Sorted list by mergeSort method: {}'.format(li))