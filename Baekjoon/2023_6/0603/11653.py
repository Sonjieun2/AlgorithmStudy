N = int(input())
num = []

for i in range(1, N+1) :
    if N%i == 0 :
        n = 0
        for j in range(1, i+1) :
            if i%j == 0 :
                n += 1
        if n == 2 :
            num.append(i)

result = []
k = 0
while N != 1 :
    if N%num[k] == 0 :
        result.append(num[k])
        N = N//num[k]
        if N in num :
            result.append(N)
            break
    else :
        k += 1

for l in range(0, len(result)) :
    print(result[l])