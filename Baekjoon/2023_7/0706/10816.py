import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

result = {num[i]:0 for i in range(M)}

for j in card :
    if j in result :
        result[j] += 1

for k in range(M) :
    print(result[num[k]], end=" ")