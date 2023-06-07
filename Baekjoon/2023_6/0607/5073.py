while True :
    A, B, C = map(int, input().split())
    if A!=0 and B!=0 and C!=0 :
        if A == B == C :
            print("Equilateral")

        elif A<B+C and B<A+C and C<A+B :
            if A==B or A==C or B==C :
                print("Isosceles")
            else :
                print("Scalene")
        
        else :
            print("Invalid")
            
    else :
        break

'''
while True :
    A, B, C = map(int, input().split())
    if A!=0 and B!=0 and C!=0 :
        if A == B == C :
            print("Equilateral")

        elif A<B+C and B<A+C and C<A+B :
            if A==B or A==C or B==C :
                print("Isosceles")
            else :
                print("Scalene")
        
        else :
            print("Invalid")
            
    else :
        break

처음엔 이렇게 했는데 계속 틀린 이유
: 1 5 1 처럼 두 변의 길이가 같은데 삼각형 세 변의 조건을 무시하는 경우
  Invalid가 맞는 출력이지만 두 변의 길이를 먼저 계산해 Isosceles가 출력됐다.
'''