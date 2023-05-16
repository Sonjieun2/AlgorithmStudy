N, M = map(int, input().split())
bucket = list(range(1, N+1))

for _ in range(M) :
    i, j, k = map(int, input().split())
    i = i-1
    j = j-1
    k = k-1

    bucket = bucket[:i] + bucket[k:j+1] + bucket[i:k] + bucket[j+1:]

for n in range(0, N) :
    print(bucket[n], end=" ")