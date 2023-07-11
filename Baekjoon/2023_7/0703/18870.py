import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
A = list(sorted(set(arr)))

result = {A[i]:i for i in range(len(A))}

for j in arr :
    print(result[j], end=" ")