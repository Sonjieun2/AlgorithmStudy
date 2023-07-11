str = input()
word = list(str)
l = len(word)

N = 2
while N <= l :
    for i in range(l-N+1) :
        S = str[i:i+N]
        word.append(S)
    N += 1

word = set(word)

print(len(word))