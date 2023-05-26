word = input().lower()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia :
    if i in word :
        word = word.replace(i, "*")
    
    else :
        continue
    
print(len(word))