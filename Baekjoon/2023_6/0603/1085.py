x, y, w, h = map(int, input().split())
distance = 0

if x <= w//2 :
    distance = x

else :
    distance = w-x

if y <= h//2 :
    if distance > y :
        distance = y

else :
    if distance > h-y :
        distance = h-y

print(distance)