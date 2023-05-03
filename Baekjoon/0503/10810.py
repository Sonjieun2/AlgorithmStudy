N, M = map(int, input().split())
str = [0 for _ in range(100)]

if 1<=N<=100 and 1<=M<=100 :
    for _ in range (M) :
        i, j, k = map(int, input().split())
        for n in range(i-1, j) :
            str[n] = k
        
for m in range (N) :
    print(str[m] , end=" ")