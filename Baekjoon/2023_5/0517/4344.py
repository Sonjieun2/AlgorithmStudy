C = int(input())
student = []

for _ in range(C) :
    score = list(map(int, input().split()))
    sum = 0
    avg = 0

    for i in range(1, len(score)) :
        sum = sum+score[i]
    
    avg = sum/score[0]

    up = 0
    for i in range(1, len(score)) :
        if score[i] > avg :
            up = up+1
    
    up = (f'{(up/score[0]*100):.3f}')
    student.append(up)

for j in range(0, C) :
    print(student[j] + "%")