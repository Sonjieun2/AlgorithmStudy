import sys
input = sys.stdin.readline

N = int(input())
arr = set(list(map(int, input().split())))

M = int(input())
card = list(map(int, input().split()))

result = [0] * M

for i in range(M) :
    if card[i] in arr :
        result[i] = 1

print(*result)