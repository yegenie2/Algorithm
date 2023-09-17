t = int(input())

time = [300, 60, 10]
count = []
if t % 10 !=0 :
    print(-1)
else :
    for i in time:
        count.append(t//i)
        t %= i
    print(*count)