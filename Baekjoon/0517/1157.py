word = input().upper()
word_uniq = list(set(word))

c = []
for i in word_uniq :
    c.append(word.count(i))

if c.count(max(c)) > 1 :
    print("?")

else :
    max_index = c.index(max(c))
    print(word_uniq[max_index])