sum = []
k = 0
while True :
    A, B = map(int, input().split())
    if A!=0 and B!=0 :
        sum.append(A+B)
        k = k+1
    
    else :
        break

for i in range(0, k) :
    print(sum[i])