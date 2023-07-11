a1, a0 = map(int, input().split())
C = int(input())
n0 = float(input())

if ((a1*n0)+a0) <= C*n0 and a1 <= C :
    print("1")

else :
    print("0")