sum = []
for i in range(9) :
    sum.append(int(input()))

print(max(sum))
print(sum.index(max(sum))+1)