N = int(input())
num = 0

for _ in range(N) :
    word = input()
    if len(word) > 1 and len(list(set(word))) != 1 :
        for j in range(0, len(word)-1) :
            if word[j] != word[j+1] and word[j] in word[j+2:]:
                num = num+1
                break

print(N-num)