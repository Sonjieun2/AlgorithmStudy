N = int(input())
dance = set()

for i in range(N) :
    A, B = input().split()
    if "ChongChong" in dance :
        if A in dance :
            dance.add(B)

        elif B in dance :
            dance.add(A)
             
    else :
        if A == "ChongChong" or B == "ChongChong" :
            dance.add(A)
            dance.add(B)
    
        else :
            continue

print(len(dance))