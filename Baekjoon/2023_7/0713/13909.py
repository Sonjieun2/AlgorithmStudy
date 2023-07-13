import sys
input = sys.stdin.readline

N = int(input())
x = 1
count = 0

while x*x <= N :
    count += 1
    x += 1

print(count)