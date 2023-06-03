n = int(input())
sum = 0

for _ in range(n) :
    if n != 0 :
        sum = sum+n
        n = n-1
    
    else :
        break

print(sum)