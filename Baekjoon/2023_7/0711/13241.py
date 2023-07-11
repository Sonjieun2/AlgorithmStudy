A, B = map(int, input().split())

def gcd(A, B) :
    if A%B != 0 :
        return gcd(B, A%B)
    
    else :
        return B

def lcm(A, B) :
    return A*B//gcd(A, B)

print(lcm(A, B))