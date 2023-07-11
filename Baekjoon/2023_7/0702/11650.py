import sys

N = int(input())
arr = []

for i in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()

for x in range(N) :
    print(arr[x][0], arr[x][1])