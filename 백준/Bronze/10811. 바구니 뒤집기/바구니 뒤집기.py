import sys
n,m = map(int, sys.stdin.readline().split())
basket = [x for x in range (1,n+1)]
for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)