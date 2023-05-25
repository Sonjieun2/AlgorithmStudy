N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]

for i in range(0, N) :
    A[i] = list(map(int, input().split()))

for i in range(0, N) :
    B[i] = list(map(int, input().split()))

for i in range(0, N) :
    for j in range(0, M) :
        print((A[i][j]+B[i][j]), end=" ")
    print("")