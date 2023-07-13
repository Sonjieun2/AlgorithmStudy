import sys
input = sys.stdin.readline

T = int(input())
num = [int(input()) for _ in range(T)]
arr = [1 for _ in range(max(num)+1)]
l = len(arr)

arr[0] = 0
arr[1] = 0
for i in range(2, int(l**0.5)+1) :
    if arr[i] == 1 :
        for j in range(i+i, l, i) :
            arr[j] = 0

for k in range(T) :
    count = 0
    for a in range(2, num[k]//2+1) :
        if arr[a] == 1 :
            if arr[num[k]-a] == 1 :
                count += 1
    print(count)