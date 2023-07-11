N, M = map(int, input().split())
chess = []

for i in range(N) :
    chess.append(input())

result = []

for n in range(N-7) :
    for m in range(M-7) :
        w_count = 0
        b_count = 0
        for i in range(n, n+8) :
            for j in range(m, m+8) :
                if (i+j)%2 == 0 :
                    if chess[i][j] != "B" :
                        b_count += 1
                    elif chess[i][j] != "W" :
                        w_count += 1
                
                else :
                    if chess[i][j] != "W" :
                        b_count += 1
                    elif chess[i][j] != "B" :
                        w_count += 1
        result.append(min(w_count, b_count))

print(min(result))