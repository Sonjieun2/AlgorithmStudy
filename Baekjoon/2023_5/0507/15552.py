import sys

T = int(input())
sum = []

for _ in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    sum.append(A+B)

for i in range(0, T) :
    print(sum[i])