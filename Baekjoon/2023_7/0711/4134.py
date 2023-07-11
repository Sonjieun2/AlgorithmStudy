import sys
input = sys.stdin.readline

def T(a) :
    for i in range(2, (a//2)) :
        if a%i == 0 :
            return False
    return True

N = int(input())
result = []

for j in range(N) :
    n = int(input())
    while True :
        if T(n) :
            result.append(n)
            break
        else :
            n += 1

for k in range(N) :
    print(result[k])