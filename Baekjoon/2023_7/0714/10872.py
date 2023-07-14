N = int(input())

def P(n) :
    if n == 0 :
        return 1
    else :
        return n*P(n-1)

print(P(N))