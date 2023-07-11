import sys

N = int(input())

arr = [0] * 10001

for i in range(N) :
    num = int(sys.stdin.readline())
    arr[num] += 1

for j in range(10001) :
    if arr[j] >= 1 :
        for k in range(arr[j]) :
            print(j)