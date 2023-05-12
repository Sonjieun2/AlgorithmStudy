N = int(input())
R = []

for _ in range(N) :
    n, str = input().split()
    n = int(n)
    line = []
    for i in range(0, len(str)) :
        line.append(str[i]*n)
    R.append(line)

for j in range(0, N) :
    for k in range(0, len(R[j])) :
        print(R[j][k], end="")
    print("")