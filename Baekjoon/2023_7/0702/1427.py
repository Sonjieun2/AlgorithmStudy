num = list(map(int, input()))

num.sort()
num.reverse()

for i in range(len(num)) :
    print(num[i], end="")