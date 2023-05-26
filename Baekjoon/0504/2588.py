A = int(input())
B = int(input())
num_list = list(map(int, str(B)))

num1 = A*num_list[2]
num2 = A*num_list[1]
num3 = A*num_list[0]
print(num1)
print(num2)
print(num3)

print(num1 + num2*10 + num3*100)