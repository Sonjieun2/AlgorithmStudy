import sys
input = sys.stdin.readline

N = int(input())
avg = 0
arr = []

for i in range(N) :
    num = int(input())
    arr.append(num)
    avg += num

arr.sort()

center = arr[(N//2)]
range = arr[len(arr)-1] - arr[0]

D = dict()
for j in arr :
    if j in D :
        D[j] += 1
    else :
        D[j] = 1

M = [k for k, v in D.items() if max(D.values()) == v]
if len(M) == 1 :
    mode = M[0]
else :
    mode = M[1]

print(round(avg/N))
print(center)
print(mode)
print(range)