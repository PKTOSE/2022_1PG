# Heap Sorting

def heapify(list, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[l] < list[smallest]:
        smallest = l

    if r < n and list[r] < list[smallest]:
        smallest = r

    if smallest != i:
        list[i], list[smallest] = list[smallest], list[i]

        heapify(list, n, smallest)

def heapsort(list):
    n = len(list)

    for i in range(n//2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

list = [10, 7, 3, 9, 1, 5]
print(f'Original list: {list}')
heapsort(list)
print(f'Sorted by heapsort method(min heap): {list}')