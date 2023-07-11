import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input() for _ in range(N)])
result = 0

for i in range(M) :
    str = input()
    if str in S :
        result += 1

print(result)