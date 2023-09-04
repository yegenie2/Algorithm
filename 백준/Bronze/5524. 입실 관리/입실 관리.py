n = int(input())
word = []
for _ in range(n):
    word.append(input().lower())
print(*word,sep='\n')
