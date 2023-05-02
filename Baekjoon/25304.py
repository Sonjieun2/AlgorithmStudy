X = int(input())
N = int(input())
result = 0

if 1<=X<=1000000000 and 1<=N<=100 :
    for i in range (N) :
        a, b = map(int, input().split())
        if 1<=a<=1000000 and 1<=b<=10 :
            result += a*b
    
    if result == X :
        print("Yes")
        
    else :
        print("No")