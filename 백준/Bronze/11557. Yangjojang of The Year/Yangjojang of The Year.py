t = int(input())
temp1 = []
temp2 = []
temp3 = []
for i in range(t):
    n = int(input())
    for i in range(n):
        s, l = input().split()
        temp1.append(s)
        temp2.append(int(l))
    idx = temp2.index(max(temp2))
    temp3.append(temp1[idx])
print(*temp3 , sep='\n')