word = input()
lst = [0]*26

for i in word:
    lst[ord(i)-97]+=1

print(*lst)