A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a, b) :
    if a%b != 0 :
        return gcd(b, a%b)
    else :
        return b

def lcm(a, b) :
    return a*b//gcd(a, b)

L = lcm(B, D)
X = ((L//B)*A)+((L//D)*C)

print((X//gcd(X, L)), (L//gcd(X, L))) 