N, M = map(int, input().split())
num = list(range(1, N+1))

for _ in range(M) :
    i, j = map(int, input().split())
    temp = num[i-1:j]
    temp.reverse()
    num[i-1:j] = temp

for k in range(0, N) :
    print(num[k], end=" ")