arr = ['a','A','e','E','i','I','o','O','u','U']
while 1:
    cnt = 0
    word = input()
    if word == '#':
        break 
    for i in word:
        if i in arr:
            cnt += 1
    print(cnt)