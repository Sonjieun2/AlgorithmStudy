a, b, c = map(int, input().split())

if a == b == c :
    reward = 10000+a*1000

else :
    if a == b or a == c :
        reward = 1000+a*100
    
    elif b == c :
        reward = 1000+b*100
    
    else :
        if a > b and a > c :
            reward = a*100
        
        elif b > a and b > c :
            reward = b*100
        
        else :
            reward = c*100

print(reward)