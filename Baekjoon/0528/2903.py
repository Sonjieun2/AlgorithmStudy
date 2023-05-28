N = int(input())
dot = 3

if N != 1 :
    for _ in range(N-1) :
        dot = dot+(dot-1)


print(dot*dot)