num = int(input())
location = [[0 for _ in range(1, 101)] for _ in range(1, 101)]

for i in range(num) :
    x_side, y_side = map(int, input().split())
    for row in range(x_side, x_side+10) :
        for col in range(y_side, y_side+10) :
            location[row][col] = 1

result = 0
for l in location :
    result += l.count(1)

print(result)