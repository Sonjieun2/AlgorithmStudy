student = []
noHw = [0, 0]

for i in range(28) :
    num = int(input())
    student.append(num)


for j in range(1, 31) :
    k = 0
    for i in range(28) :
        if student[i-1] != j :
            k += 1
    
    if k == 28 :
        print(j)