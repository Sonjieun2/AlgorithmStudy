num, n = map(int, input().split())
str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []

while num >= n :
    result.append(str[int(num%n)])
    num = num//n

result.append(str[num])

for i in range(len(result)-1, -1, -1) :
    print(result[i], end="")