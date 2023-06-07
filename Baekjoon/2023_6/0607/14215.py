a, b, c = map(int,input().split())

if a>=b+c or b>=a+c or c>=a+b :
    if a>b and a>c :
        a = (b+c)-1
    elif b>a and b>c :
        b = (a+c)-1
    else :
        c = (a+b)-1

print(a+b+c)
