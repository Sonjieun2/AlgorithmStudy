N = int(input())
num = list(map(int, input().split()))
min = num[0]
max = num[0]

for i in range(1, N) :
    if num[i] < min :
        min = num[i]
    
    elif num[i] > max :
        max = num[i]

print(min, max)