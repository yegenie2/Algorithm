import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

temp = []
temp.append(math.ceil(a/c))
temp.append(math.ceil(b/d))
print(l-max(temp))
