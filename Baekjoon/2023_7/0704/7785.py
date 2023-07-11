N = int(input())
dict = {}

for i in range(N) :
    name, state = input().split()
    if state == "enter" :
        dict[name] = state
    
    else :
        del dict[name]

dict = sorted(dict.keys(), reverse=True)

for j in dict :
    print(j)