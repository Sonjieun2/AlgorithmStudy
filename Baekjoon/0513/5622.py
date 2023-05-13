str = input()
num = 0
time = 0

for i in str :
    n = ord(i)
    if 65<=n<=67 :
        num = 2
    
    elif 68<=n<=70 :
        num = 3
    
    elif 71<=n<=73 :
        num = 4
    
    elif 74<=n<=76 :
        num = 5
    
    elif 77<=n<=79 :
        num = 6
    
    elif 80<=n<=83 :
        num = 7
    
    elif 84<=n<=86 :
        num = 8
    
    else :
        num = 9
    
    time = time + (num+1)

print(time)