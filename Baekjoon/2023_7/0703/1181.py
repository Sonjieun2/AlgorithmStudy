N = int(input())
arr = []
length = []

for i in range(N) :
    arr.append(input())
    length.append(len(arr[i]))

print(length)

num = [0 for _ in range(max(length))]
result = [[] for _ in range(max(length))]

for j in range(N) :
    num[length[j]-1] += 1
    result[length[j]-1].append(arr[j])

print(num)
print(result)

for k in range(len(result)) :
    if len(result[k]) > 1 :
        result[k] = list(set(result[k]))
        result[k].sort()

    for l in range(len(result[k])) :
        print(result[k][l])