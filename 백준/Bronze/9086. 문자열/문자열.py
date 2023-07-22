t = int(input())
temp = []
for i in range(t):
    word = input()
    i = len(word)
    temp.append(word[0]+word[i-1])
print(*temp, sep='\n')