import sys
n,x = map(int,input().split())
a = list(map(int, sys.stdin.readline().split()))
min_list = []
for i in range (n):
    if a[i] < x:
        value = a[i]
        min_list.append(value)
print(*min_list)