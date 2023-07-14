N, K = map(int, input().split())

def C(a) :
    if a == 0 :
        return 1
    else :
        return a*C(a-1)

if K == 0 or K == N :
    print(1)

else :
    print(C(N)//(C(K)*C(N-K)))