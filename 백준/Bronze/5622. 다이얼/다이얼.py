number =['ABC', 'DEF', 'GHI', 'JKL',
         'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
word = list(input())

for i in word:
    for j in number:
        if i in j:
            time += number.index(j)+3
print(time)