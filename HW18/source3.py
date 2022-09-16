def find(current, visited):
    if visited == total:
        return W[current][0] if W[current][0] else 202020
    if D[current][visited] > 0:
        return D[current][visited]

    cost = 202020

    for i in range(1, n):
        if (visited >> i) % 2 == 1 or W[current][i] == 202020: continue
        tmp = find(i, visited | (1<<i))
        cost = min(tmp + W[current][i], cost)

    D[current][visited] = cost
    return cost



n = 4
W = [[0, 2, 9, 202020], [1, 0, 6, 4], [202020, 7, 0, 8], [6, 3, 202020, 0]]

D = [[0]*(1<<n) for _ in range(n)]
total = (1<<n)-1

result = find(0,1)
print('최적의 cost: ', result)