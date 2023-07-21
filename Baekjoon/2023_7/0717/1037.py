import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

num.sort()
if N == 1 :
    print(num[0]**2)

else :
    print(num[0]*num[len(num)-1])