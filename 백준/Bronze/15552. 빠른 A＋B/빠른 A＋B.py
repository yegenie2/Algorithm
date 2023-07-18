import sys

t = int(sys.stdin.readline())
sum = 0
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)