num = [int(input()) for _ in range(5)]

avg = 0

for i in range(5) :
    avg += num[i]

num.sort()

print(int(avg/5))
print(num[2])