n,k = map(int, input().split())
coin =[]
temp = 0
for _ in range (n):
    coin.append(int(input()))
for i in reversed(coin):
    temp += k//i
    k = k % i
print(temp)