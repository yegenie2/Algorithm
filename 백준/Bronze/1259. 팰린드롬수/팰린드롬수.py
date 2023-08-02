answer = []

while 1:
    num = input()
    if num == '0':
        break
    r_num = ''.join(reversed(num))

    if num == r_num :
        answer.append('yes')
    else :
        answer.append('no')
print(*answer, sep='\n')