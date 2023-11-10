max_value = 0
row = 0
col = 0
for i in range(9):
    lst= list(map(int,input().split()))
    if int(max(lst))>max_value:
        max_value = max(lst)
        row = i
        col = lst.index(max(lst))
print(max_value)
print(row+1,col+1)