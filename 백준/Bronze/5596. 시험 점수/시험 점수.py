total = []
for i in range(2):
    i,m,s,e = map(int,(input().split()))
    total.append(i+m+s+e)
if total[0] == total[1]:
    print(total[0])
else:
    print(max(total))