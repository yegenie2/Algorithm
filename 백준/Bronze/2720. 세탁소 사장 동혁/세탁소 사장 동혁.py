t = int(input())

money = [25, 10, 5, 1]
for _ in range(t):
    c = int(input())
    cnt = []
    
    for i in money:
        cnt.append(c//i)
        c = c%i
    print(*cnt)
