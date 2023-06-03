N = int(input())
s = []

for _ in range(N) :
    str = input()
    s.append(str[0] + str[-1])

for i in range(0, N) :
    print(s[i])