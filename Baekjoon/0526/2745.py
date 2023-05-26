Alpa = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str, n = input().split()
n = int(n)
str = ''.join(reversed(str))
result = 0

for i in range(0, len(str)) :
    sum = Alpa.index(str[i])*(n**i)
    result += sum
    print(result)

print(result)