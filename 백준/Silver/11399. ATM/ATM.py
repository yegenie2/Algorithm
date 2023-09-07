n = int(input())
time = list(map(int, input().split()))
s_time = sorted(time)
temp = 0
lst =[]
for i in s_time:
    temp += i
    lst.append(temp)
print(sum(lst))