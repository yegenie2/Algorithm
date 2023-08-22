s = int(input())
sum = 0

for i in range(1, s+1):
    sum += i
    if s == 1:
        print(1)
        break
    if sum > s:  
        print(i-1)
        break