import sys

t = int(sys.stdin.readline().strip())
sum = 0
for i in range(1,t+1):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")