def find(current, visited):
    if visited == total:
        return (W[current][0], [current, 0]) if W[current][0] else (202020, [-1])

    # 이미 방문한 노드
    if D[current][visited] > 0:
        return (D[current][visited], [current])

    cost = 202020

    # indice는 최소 경로에 대한 방문 경로
    indice = []

    for i in range(1, n):
        if (visited >> i) % 2 == 1 or W[current][i] == 202020: continue
        tmp, h_indice = find(i, visited | (1<<i))
        # 루트가 생각 : i로 시작해서 모든 노드를 방문하고 온 비용 tmp
        # 최소 값을 찾고 방문 경로에 기록한다.
        if cost > tmp + W[current][i]:
            cost = tmp + W[current][i]
            indice = h_indice

    # 현재 노드와 함께 방문 경로 업데이트
    indice = [current]+indice
    D[current][visited] = cost
    return cost, indice

n = 5
W = [
    [0, 13, 23, 16, 5],
    [13, 0, 29, 20, 7],
    [21, 29, 0, 11, 30],
    [16, 20, 11, 0, 19],
    [5, 7, 30, 19, 0]
]

D = [[0]*(1<<n) for _ in range(n)]
total = (1<<n)-1

# 노드 0에서 출발하여 모든 노드들을 다 방문한 뒤 노드 0으로 돌아오는 최소 경로 계산
cost, indice = find(0,1)
print(f'(10): 최적의 cost={cost}, 최적의 경로={indice}')