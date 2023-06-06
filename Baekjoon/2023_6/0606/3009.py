xlist = []
ylist = []
xresult = 0
yresult = 0

for  _ in range(3) :
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)

for i in range(0, 3) :
    if xlist.count(xlist[i]) == 1 :
        xresult = xlist[i]
    
    if ylist.count(ylist[i]) == 1 :
        yresult = ylist[i]

print(xresult, yresult)