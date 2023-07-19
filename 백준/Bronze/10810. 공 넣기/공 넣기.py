import sys

n,m = map(int, sys.stdin.readline().split())
basket = [0]*n
for i in range(m):
    i,j,k = map(int, sys.stdin.readline().split())
    for idx in range(i,j+1):
        basket[idx-1] = k
print(*basket)
