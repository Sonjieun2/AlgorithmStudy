A, B, V = map(int, input().split())
#A : 낮에 올라가는 거리, B : 밤에 미끄러지는 거리, V : 정상까지의 거리

day = (V-B)/(A-B)

if day == int(day) :
    print(int(day))

else :
    print(int(day)+1)