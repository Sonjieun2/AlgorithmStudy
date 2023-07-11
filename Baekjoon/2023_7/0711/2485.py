import sys
input = sys.stdin.readline

def gcd(a, b) :
    if a%b != 0 :
        return gcd(b, a%b)
    else :
        return b

N = int(input())
tree = int(input())
distance = []

for i in range(N-1) :
    T = int(input())
    distance.append(T-tree)
    tree = T

g = distance[0]
for j in range(1, N-1) :
    g = gcd(g, distance[j])

result = 0
for num in distance :
    result += num//g-1

print(result)