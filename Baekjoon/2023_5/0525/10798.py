word = [[0]*15 for _ in range(5)]
result = ""

for i in range(5) :
    w = list(input())
    w_len = len(w)

    for j in range(w_len) :
        word[i][j] = w[j]

for k in range(15) :
    for l in range(5) :
        if word[l][k] == 0  :
            continue
        else :
            result = result + word[l][k]

print(result)