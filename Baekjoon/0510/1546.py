N = int(input())
score = list(map(int, input().split()))
max = score[0]
avg = 0

for i in range(1, N) :
    if max < score[i] :
        max = score[i]

for j in range(0, N) :
    score[j] = score[j]/max*100
    avg = avg+score[j]

print(avg/N)