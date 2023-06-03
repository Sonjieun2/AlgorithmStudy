T = int(input())
sum = []

for _ in range(T) :
    A, B = map(int, input().split())
    sum.append(A+B)

for i in range(0, T) :
    print("Case #" + str(i+1) + ":", sum[i])