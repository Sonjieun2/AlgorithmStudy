N, X = map(int, input().split())
A = list(map(int, input().split()))
num = []
k = 0

for i in range(0, N) :
    if A[i] < X :
        num.append(A[i])
        k = k+1
    
for j in range(0, k) :
    print(num[j], end=" ")