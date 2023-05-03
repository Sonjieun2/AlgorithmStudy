N, M = map(int, input().split())
k = 0

if 1<=N<=100 and 1<=M<=100 :
    basket = range(1, N+1)
    basket = list(basket)

    for _ in range(M) :
        i, j = map(int, input().split())
        k = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = k
    
    for n in range(N) :
        print(basket[n], end=" ")