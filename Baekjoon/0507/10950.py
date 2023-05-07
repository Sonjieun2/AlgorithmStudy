T = int(input())
num = []

for _ in range(T) :
    A, B = map(int, input().split())
    k = A+B
    num.append(k)

for C in range(0, T) :
    print(num[C])