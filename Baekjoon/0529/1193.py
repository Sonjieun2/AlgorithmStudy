N = int(input())

line = 0
end = 0

while N > end :
    line += 1
    end += line

n = end-N
if line%2 == 0 :
    m = line-n
    s = n+1
else :
    m = n+1
    s = line-n

print(m, "/", s, sep="")