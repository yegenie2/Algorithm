from queue import PriorityQueue

n = int(input())
card = PriorityQueue()
lst = []
for _ in range(n):
    card.put(int(input()))

for i in range(n-1):
    temp = card.get(card)+card.get(card)
    card.put(temp)
    lst.append(temp)
print(sum(lst))