x,y,z = map(int,input().split())

if x == y == z :
    prize = 10000 + (x)*1000
elif x == y:
    prize = 1000 + (x)*100
elif y == z:
    prize = 1000 + (y)*100
elif x == z:
    prize = 1000 + (x)*100
else :
    prize = max(x,y,z)*100

print(prize)