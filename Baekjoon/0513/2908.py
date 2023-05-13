num1, num2 = input().split()
num_1 = ""
num_2 = ""

for i in num1 :
    num_1 = i + num_1

for j in num2 :
    num_2 = j + num_2

if int(num_1) < int(num_2) :
    print(num_2)

else :
    print(num_1)