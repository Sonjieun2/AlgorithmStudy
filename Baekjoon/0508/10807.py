N = int(input())
n = []
k = 0

n = list(map(int, input().split()))

v = int(input())

for i in range(0, N) :
    if n[i] == v :
        k = k+1
    
print(k)