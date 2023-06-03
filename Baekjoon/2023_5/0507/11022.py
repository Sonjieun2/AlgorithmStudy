T = int(input())
sum = []
num1 = []
num2 = []

for _ in range(T) :
    A, B = map(int, input().split())
    num1.append(A)
    num2.append(B)
    sum.append(A+B)

for i in range(0, T) :
    print("Case #" + str(i+1) + ":", num1[i], "+", num2[i], "=", sum[i])