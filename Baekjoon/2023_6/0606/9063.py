mable = int(input())
Xside = []
Yside = []

for _ in range(mable) :
    x, y = map(int, input().split())
    Xside.append(x)
    Yside.append(y)

Xlength = max(Xside) - min(Xside)
Ylength = max(Yside) - min(Yside)

print(Xlength*Ylength)