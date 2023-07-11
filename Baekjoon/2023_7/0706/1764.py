N, M = map(int, input().split())
name1 = []
name2 = []

for i in range(N) :
    name1.append(input())

for j in range(M) :
    name2.append(input())

name1 = set(name1)
name2 = set(name2)

result = name1 & name2
result = list(result)
result.sort()

print(len(result))
for k in range(len(result)) :
    print(result[k])