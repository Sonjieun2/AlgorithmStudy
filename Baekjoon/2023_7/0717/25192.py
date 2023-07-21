import sys
input = sys.stdin.readline

N = int(input())
chat = set()
result = 0

for i in range(N) :
    name = input().strip()
    if name == "ENTER" :
        result += len(chat)
        chat.clear()
    else :
        if name not in chat :
            chat.add(name)

result += len(chat)
print(result)