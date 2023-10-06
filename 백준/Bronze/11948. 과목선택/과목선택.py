sub1 = []
sub2 = []

for i in range(4):
    sub1.append(int(input()))
for j in range(2):
    sub2.append(int(input()))
sub1.sort()
sub1.pop(0)
sub2.sort()
sub2.pop(0)
print(sum(sub1)+sum(sub2))