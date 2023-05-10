num = []
k = 1
for i in range(10) :
    N = int(input())
    n = N%42
    num.append(n)

num.sort()
for i in range(0, 9) :
    if num[i] != num[i+1] :
        k = k+1

print(k)