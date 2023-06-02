num = 0

while num != -1 :
    num = int(input())
    m = []
    sum = 0
    if num == -1 :
        break
    else :
        for i in range(1, num) :
            if num%i == 0 :
                m.append(i)
                sum += i
    
        if sum == num :
            print(num, "= ", end="")
            for j in range(0, len(m)) :
                if m[j] != m[(len(m)-1)] :
                    print(m[j], "+ ", end="")
                else :
                    print(m[j])
    
        else :
            print(num, "is NOT perfect.")