import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def T(n) :
    if n != 0 and n != 1 :
        for i in range(2, int((n**0.5)+1)) :
            if n%i == 0 :
                return False
        return True

result = []

for j in range(M, N+1) :
    if T(j) :
        result.append(j)

for k in range(len(result)) :
    print(result[k])