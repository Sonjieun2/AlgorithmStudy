from math import gcd

T = int(input())
result = []

for i in range(T) :
    A, B = map(int, input().split())
    result.append(A*B//gcd(A, B))

for j in range(T) :
    print(result[j])