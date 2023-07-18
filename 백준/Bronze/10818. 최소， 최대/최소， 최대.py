import sys
n = int(input())
m = list(map(int,sys.stdin.readline().split()))
print(min(m), max(m))