p, q = map(int, input().split())
num = 0

for i in range(1, p+1) :
    if p%i == 0 :
        num += 1

if num > q :
    divisor = [0 for _ in range(num)]
else :
    divisor = [0 for _ in range(q)]

l = len(divisor)
for i in range(1, p+1) :
    if p%i == 0 :
        divisor[l-1] = i
        l -= 1

divisor.reverse()
print(divisor[q-1])