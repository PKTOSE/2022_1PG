def fibo(n):
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

def fibo_dp(n):
    tmp = [0 for index in range(n+1)]
    tmp[0] = 0
    tmp[1] = 1

    for index in range(2, n+1):
        tmp[index] = tmp[index-1] + tmp[index-2]
    return tmp[n]

num = 10
print('계산 by 순환 알고리즘: ', fibo(num))
print('계산 by 동적프로그래밍: ', fibo_dp(num))