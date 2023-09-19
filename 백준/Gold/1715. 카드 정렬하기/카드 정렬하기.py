from heapq import *

n = int(input())
card = []
lst = []
for _ in range(n):
    heappush(card,int(input()))
for i in range(n-1):
    temp = heappop(card)+heappop(card)
    heappush(card,temp)
    lst.append(temp)
print(sum(lst))
