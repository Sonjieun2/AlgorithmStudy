N = int(input())
M = [[0]*4 for _ in range(N)]

for i in range(N) :
    money = int(input())
    if money >= 25 :
        M[i][0] = money//25
        money = money%25
    
    if money >= 10 :
        M[i][1] = money//10
        money = money%10
    
    if money >= 5 :
        M[i][2] = money//5
        money = money%5
    
    if money >= 1 :
        M[i][3] = money//1


for i in range(0, N) :
    for j in range(0, 4) :
        print(M[i][j], end=" ")
    print("")