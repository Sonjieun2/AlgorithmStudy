N, k = map(int, input().split())
score = [*map(int, input().split())]

score.sort()
score.reverse()

print(score[k-1])