t = int(input())
answer =[]
for i in range(t):
    r,s = input().split()
    word = list(s)
    result=""
    for j in range(len(word)):
        result += word[j]*int(r)
    answer.append(result)     
print(*answer, sep="\n")
