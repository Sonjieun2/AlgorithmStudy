M = int(input())
N = int(input())
result = []
sum = 0

for i in range(M, N+1) :
    m = 0
    for j in range(1, i+1) :
        if i%j == 0 :
            m += 1
    if m == 2 :
        result.append(i)
        sum += i

if sum == 0 :
    print(-1)

else :
    print(sum)
    print(min(result))