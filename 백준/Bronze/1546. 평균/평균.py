import sys
n = int(input())

score = list(map(int, sys.stdin.readline().split()))
m = max(score)
for i in range(n):
    score[i] = score[i]/m*100   
avg = sum(score)/n
print(avg)