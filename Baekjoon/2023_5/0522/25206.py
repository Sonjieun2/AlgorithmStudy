sum = 0
s = 0

for _ in range(20) :
    subject, n, grade = input().split()
    num = float(n)
    if grade == "P" :
        continue
    else :
        if grade == "A+" :
            score = 4.5
        elif grade == "A0" :
            score = 4.0
        elif grade == "B+" :
            score = 3.5
        elif grade == "B0" :
            score = 3.0
        elif grade == "C+" :
            score = 2.5
        elif grade == "C0" :
            score = 2.0
        elif grade == "D+" :
            score = 1.5
        elif grade == "D0" :
            score = 1.0
        elif grade == "F" :
            score = 0.0
        
    sum = float(sum+(num*score))
    s = float(s+num)

print(round((sum/s), 6))