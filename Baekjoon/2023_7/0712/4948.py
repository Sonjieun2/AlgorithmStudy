import sys
input = sys.stdin.readline

N = 123456*2+1
arr = [1]*N

for i in range(N) :
    if i != 0 and i != 1 :
        for j in range(2, int(i**0.5)+1) :
            if i%j == 0 :
                arr[i] = 0
                break

result = []

while True :
    num = int(input())
    count = 0
    if num == 0 :
        break
    for k in range(num+1, (num*2)+1) :
        count += arr[k]
    result.append(count)

for a in range(len(result)) :
    print(result[a])