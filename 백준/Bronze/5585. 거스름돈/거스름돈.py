n = int(input())

money = [500, 100, 50, 10, 5, 1]
change = 1000-n
cnt = 0

for i in money:
    cnt += change //i
    change = change %i
print(cnt)