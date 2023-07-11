N = int(input())
num = 666
result = []

while True :
    if "666" in str(num) :
        result.append(num)
    
    num = int(num)
    num += 1

    if len(result) == N :
        break

print(result[N-1])