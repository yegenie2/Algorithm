a, b = map(int, input().split())
c, d = map(int, input().split())
basket = []
basket.append(a+d)
basket.append(b+c)
print(min(basket))