n = int(input())
tmp = []
for i in range(n):
    score = 0
    cnt = 0
    word = input()
    for j in range(len(word)):
        if word[j] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    
    tmp.append(score)
print(*tmp, sep='\n') 