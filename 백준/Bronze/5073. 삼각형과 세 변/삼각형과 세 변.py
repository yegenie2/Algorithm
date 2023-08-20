answer = []
while 1:

    x, y, z = map(int, input().split())

    if ( x == y == z == 0):
        break
    
    if ( x >= y + z ) or ( y >= x + z) or (z >= x + y):
        answer.append('Invalid')
    elif x == y == z :
        answer.append('Equilateral')
    elif x == y or y == z or x == z :
        answer.append('Isosceles')
    else : 
        answer.append('Scalene')

print(*answer , sep='\n')