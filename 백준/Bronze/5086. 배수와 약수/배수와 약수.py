answer = []
while 1:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    if (y % x == 0):
        answer.append('factor')
    elif (x % y == 0):
        answer.append('multiple')
    elif (x % y != 0):
        answer.append('neither')
print(*answer, sep='\n')