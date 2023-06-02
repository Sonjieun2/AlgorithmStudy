N = int(input())
num = list(map(int, input().split()))
result = 0

for i in range(0, N) :
    m = 0
    for j in range(1, num[i]+1) :
        if num[i]%j == 0 :
            m += 1
    
    if m == 2 :
        result += 1

print(result)