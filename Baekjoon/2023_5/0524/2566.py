A = [[0 for _ in range(9)] for _ in range(9)]

for i in range(0, 9) :
    A[i] = list(map(int, input().split())) 

max = 0
max_row = 0
max_column = 0

for i in range(0, 9) :
    for j in range(0, 9) :
        if A[i][j] > max :
            max = A[i][j]
            max_row = i
            max_column = j
        
print(max)
print(max_row+1, max_column+1)