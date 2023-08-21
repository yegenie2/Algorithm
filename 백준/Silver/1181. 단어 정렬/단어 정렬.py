n = int(input())
word =[]
for _ in range(n):
    word.append(input())
word = sorted(list(set(word)), key=lambda x: (len(x),x) )
print(*word, sep='\n')