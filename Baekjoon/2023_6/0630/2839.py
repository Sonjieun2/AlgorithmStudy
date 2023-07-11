N = int(input())

sugar = 0

if N >= 3 :
    while N%5 != 0 :
        N = N-3
        sugar += 1
        if N == 0 :
            break
        elif N < 3 :
            sugar = -1
            break
    
    if N%5 == 0 :
        sugar += N//5
    
    else :
        sugar = -1

else :
    sugar = -1

print(sugar)