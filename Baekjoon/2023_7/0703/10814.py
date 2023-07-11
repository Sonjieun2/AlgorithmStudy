N = int(input())
arr = []

for i in range(N) :
    arr.append(list(input().split()))
    arr[i][0] = int(arr[i][0])

arr.sort(key=lambda x:x[0])

for j in range(N) :
    print(arr[j][0], arr[j][1])