remain=[]
for i in range(10):
    a = int(input())%42
    remain.append(a)
remain = set(remain)
print(len(remain))
