# Quick Sorting

def partition(list:list, low, high):
    i = (low-1)
    pivot = list[high]

    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i+1], list[high] = list[high], list[i+1]
    return (i+1)

def quickSort(li:list, low, high):
    if low < high:
        pi = partition(li, low, high)

        quickSort(li, low, pi-1)
        quickSort(li, pi+1, high)

li = [10, 7, 3, 9, 1, 5]
print('Original list: {}'.format(li))
n = len(li); quickSort(li, 0, n-1)
print('Sorted list by quicksort method: {}'.format(li))
