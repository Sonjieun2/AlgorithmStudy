import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocket_name = {}
pocket_num = {}

for i in range(1, N+1) :
    name = input().strip()
    pocket_name[name] = i
    pocket_num[i] = name

result = []

for j in range(M) :
    item = input().strip()
    if item.isdigit() == True :
        I = int(item)
        result.append(pocket_num[I])
    else :
        result.append(pocket_name[item])

for k in range(len(result)) :
    print(result[k])