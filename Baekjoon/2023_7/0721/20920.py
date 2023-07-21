import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

D = dict()
for i in range(N) :
    W = input().rstrip()
    if len(W) >= M :
        if W in D :
            D[W] += 1
        else :
            D[W] = 1
word_sort = dict(sorted(D.items(), key=lambda x:(-x[1], -len(x[0]), x[0])))
word_key = list(word_sort.keys())
for j in word_key :
    print(j)